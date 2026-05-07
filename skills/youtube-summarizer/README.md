# youtube-summarizer

YouTube 영상 자막을 추출하고 한국어로 상세 요약을 만드는 스킬입니다.

## 특징

- 한국어 프롬프트와 한국어 요약 출력 우선 지원
- `ko`, `en`, `ja` 순서로 자막 추출 시도
- 한국어 자막이 없어도 사용 가능한 자막을 바탕으로 한국어 요약 생성
- `uv run --with youtube-transcript-api`를 사용해 프로젝트 환경을 오염시키지 않고 실행
- 원문 자막 저장 및 Markdown 요약 저장 워크플로 지원

## 예시

```text
이 유튜브 영상 한국어로 요약해줘: https://youtu.be/VIDEO_ID
```

```text
https://www.youtube.com/watch?v=VIDEO_ID 자막 추출하고 핵심 내용 정리해줘
```

## 자막 추출 명령

```bash
uv run --with youtube-transcript-api skills/youtube-summarizer/scripts/extract-transcript.py "https://youtu.be/VIDEO_ID" --languages ko,en,ja --output /tmp/youtube-transcript.json
```

## 제한사항

- 영상, 오디오 파일은 다운로드하지 않습니다.
- 공개 영상이면서 자막 또는 자동 생성 자막이 있어야 합니다.
- 비공개, 연령 제한, 삭제된 영상은 처리할 수 없습니다.

## 출처

Based on `sickn33/antigravity-awesome-skills/skills/youtube-summarizer`, adapted for Korean-first usage in this repository.
