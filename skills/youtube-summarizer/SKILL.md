---
name: youtube-summarizer
description: YouTube 영상 URL에서 자막을 추출하고 한국어로 상세 요약을 작성합니다. Use this skill whenever the user provides a YouTube URL and asks to summarize, recap, extract a transcript, analyze video contents, or create Korean notes from a video, including Korean prompts such as "유튜브 요약", "영상 정리", "자막 추출", or "한국어로 요약".
allowed-tools: Bash, Read, Write
---

# YouTube Summarizer Korean

YouTube 영상의 공개 자막을 가져와 한국어 중심의 상세 요약을 만든다. 원본은 `sickn33/antigravity-awesome-skills`의 `youtube-summarizer`이며, 이 버전은 한국어 요청과 한국어 출력에 맞게 조정되어 있다.

## Use When

- 사용자가 YouTube URL을 주고 요약, 정리, 분석, 노트 작성을 요청한다.
- 사용자가 영상 자막을 추출하거나 저장하고 싶어 한다.
- 사용자가 영어 또는 다른 언어 영상 내용을 한국어로 이해하고 싶어 한다.
- 사용자가 강의, 인터뷰, 컨퍼런스, 튜토리얼 영상을 참고 문서로 만들고 싶어 한다.

## Korean Policy

- 기본 출력 언어는 한국어다.
- 사용자가 다른 출력 언어를 명시하면 그 언어를 따른다.
- 자막은 `ko`를 우선 시도하고, 없으면 `en`, `ja` 순으로 시도한다.
- 한국어 자막이 없어도 사용자가 한국어 요약을 요청했다면 사용 가능한 자막을 바탕으로 한국어로 요약한다.
- 원문 핵심 용어는 필요하면 괄호 안에 병기한다. 예: 강화학습(reinforcement learning)

## Workflow

1. YouTube URL 또는 video ID를 확인한다.
2. 번들 스크립트로 자막을 추출한다.
3. 추출된 자막을 읽고 한국어로 구조화된 요약을 작성한다.
4. 사용자가 저장을 요청하면 Markdown 파일로 저장한다.

## Transcript Extraction

Use `uv run --with youtube-transcript-api` so the dependency does not need to be installed into the user's project:

```bash
uv run --with youtube-transcript-api skills/youtube-summarizer/scripts/extract-transcript.py "YOUTUBE_URL_OR_VIDEO_ID" --languages ko,en,ja --output /tmp/youtube-transcript.json
```

To list available transcript languages:

```bash
uv run --with youtube-transcript-api skills/youtube-summarizer/scripts/extract-transcript.py "YOUTUBE_URL_OR_VIDEO_ID" --list
```

If `uv` is unavailable, explain that this skill expects `uv` for isolated Python dependency execution and ask whether the user wants an alternative installation approach.

## Error Handling

- Invalid URL: ask for a complete YouTube URL such as `https://www.youtube.com/watch?v=VIDEO_ID` or `https://youtu.be/VIDEO_ID`.
- No transcript: explain that the video must have manual or auto-generated captions.
- Private, removed, age-restricted, or unavailable video: ask the user for a public accessible video.
- Dependency failure: report the exact command that failed and the stderr message.

## Summary Format

Use this structure unless the user requests a different format:

```markdown
# [영상 제목 또는 YouTube video ID]

**URL:** [URL]
**자막 언어:** [detected or requested language]
**요약 언어:** 한국어

## 핵심 요약

[영상 전체 주장을 3-6문장으로 압축]

## 상세 정리

### 1. [주제]

[핵심 설명, 근거, 예시]

### 2. [주제]

[핵심 설명, 근거, 예시]

## 주요 인사이트

- **[인사이트]:** [왜 중요한지]

## 용어와 개념

- **[용어]:** [문맥 속 의미]

## 실행 항목 또는 적용점

- [시청자가 실제로 적용할 수 있는 점]

## 한 줄 결론

[가장 중요한 메시지]
```

## Saving Output

When the user asks to save the result, write Markdown under the current workspace using a clear filename:

```text
youtube-summary-{video_id}-{YYYY-MM-DD}.md
```

If the user asks for the raw transcript too, append it under:

````markdown
## 원문 자막

```text
[transcript]
```
````

## Constraints

- Do not download video or audio. Extract text transcripts only.
- Do not invent metadata that was not fetched. If title, channel, or duration are unavailable, omit them or mark as unknown.
- Preserve important numbers, names, URLs, code snippets, and claims from the transcript.
- For long transcripts, summarize by sections first, then synthesize globally so important details are not lost.
