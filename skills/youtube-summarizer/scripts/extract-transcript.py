#!/usr/bin/env python3
"""Extract a YouTube transcript as plain text or JSON.

Usage:
  uv run --with youtube-transcript-api extract-transcript.py URL_OR_ID
  uv run --with youtube-transcript-api extract-transcript.py URL_OR_ID --languages ko,en,ja --output transcript.json
  uv run --with youtube-transcript-api extract-transcript.py URL_OR_ID --list
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")


def parse_video_id(value: str) -> str:
    value = value.strip()
    if VIDEO_ID_RE.fullmatch(value):
        return value

    patterns = [
        r"(?:youtube\.com/watch\?.*?[?&]?v=)([A-Za-z0-9_-]{11})",
        r"(?:youtube\.com/embed/)([A-Za-z0-9_-]{11})",
        r"(?:youtube\.com/shorts/)([A-Za-z0-9_-]{11})",
        r"(?:youtu\.be/)([A-Za-z0-9_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, value)
        if match:
            return match.group(1)

    raise ValueError("Invalid YouTube URL or video ID")


def split_languages(value: str) -> list[str]:
    languages = [item.strip() for item in value.split(",") if item.strip()]
    return languages or ["ko", "en", "ja"]


def segment_to_dict(segment: Any) -> dict[str, Any]:
    if isinstance(segment, dict):
        return {
            "text": segment.get("text", ""),
            "start": segment.get("start"),
            "duration": segment.get("duration"),
        }

    return {
        "text": getattr(segment, "text", ""),
        "start": getattr(segment, "start", None),
        "duration": getattr(segment, "duration", None),
    }


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def fetch_transcript(video_id: str, languages: list[str]) -> tuple[list[dict[str, Any]], str | None]:
    from youtube_transcript_api import YouTubeTranscriptApi

    try:
        raw_segments = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        return [segment_to_dict(item) for item in raw_segments], None
    except AttributeError:
        api = YouTubeTranscriptApi()
        fetched = api.fetch(video_id, languages=languages)
        raw_segments = getattr(fetched, "snippets", fetched)
        language_code = getattr(fetched, "language_code", None)
        return [segment_to_dict(item) for item in raw_segments], language_code


def list_transcripts(video_id: str) -> list[dict[str, Any]]:
    from youtube_transcript_api import YouTubeTranscriptApi

    try:
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)
    except AttributeError:
        transcript_list = YouTubeTranscriptApi().list(video_id)

    transcripts = []
    for transcript in transcript_list:
        transcripts.append(
            {
                "language": getattr(transcript, "language", "unknown"),
                "language_code": getattr(transcript, "language_code", "unknown"),
                "is_generated": bool(getattr(transcript, "is_generated", False)),
                "is_translatable": bool(getattr(transcript, "is_translatable", False)),
            }
        )
    return transcripts


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Extract a YouTube transcript")
    parser.add_argument("video", help="YouTube URL or 11-character video ID")
    parser.add_argument(
        "--languages",
        default="ko,en,ja",
        help="Comma-separated preferred transcript languages. Default: ko,en,ja",
    )
    parser.add_argument("--output", help="Write JSON output to this path")
    parser.add_argument("--list", action="store_true", help="List available transcript languages")
    parser.add_argument("--text", action="store_true", help="Print transcript text only")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        video_id = parse_video_id(args.video)
        languages = split_languages(args.languages)

        if args.list:
            payload = {"video_id": video_id, "transcripts": list_transcripts(video_id)}
        else:
            segments, detected_language = fetch_transcript(video_id, languages)
            text = clean_text(" ".join(segment["text"] for segment in segments))
            payload = {
                "video_id": video_id,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "requested_languages": languages,
                "detected_language": detected_language,
                "segment_count": len(segments),
                "character_count": len(text),
                "transcript": text,
            }

        if args.output:
            Path(args.output).write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

        if args.text and not args.list:
            print(payload["transcript"])
        else:
            print(json.dumps(payload, ensure_ascii=False, indent=2))

        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
