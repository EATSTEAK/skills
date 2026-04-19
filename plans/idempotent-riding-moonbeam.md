## Context
Python 작업에서 에이전트가 `python`, `pip`, `venv`를 습관적으로 직접 쓰지 않도록, 모든 Python 관련 작업을 `uv` 중심으로 유도하는 짧은 skill을 추가한다. 목표는 새 skill 하나로 실행, 의존성 관리, 일회성 도구 실행, 레거시 예외를 일관되게 안내하는 것이다.

## Recommended approach
1. `skills/use-uv/SKILL.md`를 새로 만든다.
2. frontmatter는 `name: use-uv`와 1줄 description만 둔다. description은 “Python 작업 전반에서 uv를 기본으로 사용하게 하고, Python 코드/의존성/가상환경 작업에서 트리거된다”는 뜻을 담는다.
3. 본문은 7~8줄의 짧은 명령형 지침으로 작성한다. 별도 헤더 없이 간결하게 유지한다.
4. 본문 우선순위는 다음 순서로 둔다: 직접 `pip`/`python`/`venv` 호출 금지 → `uv init` → `uv add`/`uv remove` → `uv run` → `uv sync` → `uvx` → `uv pip`는 레거시 호환시에만 허용.
5. 지침은 일반 Python 프로젝트 기준으로 쓰고, 프로젝트 컨텍스트가 필요한 도구(`pytest` 등)는 `uv run`을 쓰도록 분명히 적는다.
6. `README.md`의 Available skills 섹션에 `use-uv` 항목을 추가해 설치 대상과 경로를 노출한다.

## Critical files
- `skills/use-uv/SKILL.md` — 새 skill 본체
- `README.md` — skill 목록 갱신
- `skills/research-first/SKILL.md` — 기존 짧은 skill 형식 참조

## Reuse / patterns
- `skills/research-first/SKILL.md`의 frontmatter 구조와 짧은 명령형 본문 패턴을 그대로 따른다.
- 리서치한 uv 규칙은 `uv run`, `uv add/remove`, `uv sync`, `uvx`, `uv pip(레거시 전용)`까지만 포함해 과도한 설명을 피한다.

## Verification
- `skills/use-uv/SKILL.md`가 올바른 frontmatter(`name`, `description`)를 갖는지 확인한다.
- 본문이 7~8줄 내외의 짧은 명령형 지침인지 확인한다.
- `README.md`에 `use-uv` 항목과 경로가 기존 형식대로 추가됐는지 확인한다.
- 최종 문안이 Python 사용 시 `pip`나 `python` 직접 호출보다 `uv`를 우선하도록 충분히 명확한지 검토한다.
