# Context
The user wants this repository to become a public skills repository that can be installed via Vercel’s `npx skills add <owner/repo>` workflow and discoverable on skills.sh. The current repo does not yet contain any installable skill layout: there is no `skills/` directory, no root `SKILL.md`, no `package.json`, no manifest/index file, and no `skills.sh` script. The only relevant installability requirement confirmed from research is that the skills CLI installs from a GitHub repo and discovers directory-based skills centered on `SKILL.md` files.

# Research findings
- `skills.sh` is the public directory/registry, not a script file to add to this repo.
- Install commands are:
  - `npx skills add <owner/repo>`
  - `npx skills add <owner/repo> --skill <skill-name>`
- The CLI discovers skills from common locations including `skills/`, `.claude/skills/`, and `.agents/skills/`, with recursive fallback.
- A skill is directory-based and centered on `SKILL.md` with YAML frontmatter containing at least `name` and `description`.
- No verified central index/manifest file is required for installability from the docs we found.
- Therefore, the safest installable repo shape is a top-level `skills/` directory containing one subdirectory per skill.

# Recommended approach
Restructure this repo into a conventional skills repository for the Vercel skills CLI.

1. Create a top-level `skills/` directory.
2. Move or copy the existing `research-first` skill into `skills/research-first/SKILL.md` so the repo is installable with `npx skills add <owner/repo> --skill research-first`.
3. Add a concise human-readable repo index file (likely `README.md`) listing available skills, install commands, and one-line descriptions.
4. Do not invent an unverified machine registry format unless we find a confirmed spec later.
5. Keep `.claude/skills/research-first/SKILL.md` only if you want a local working copy too; otherwise prefer the repo-distribution path under `skills/` as the source of truth.

# Critical files to create or modify
- `/Users/koohyomin/Projects/skills/skills/research-first/SKILL.md`
- `/Users/koohyomin/Projects/skills/README.md`
- Optional: `/Users/koohyomin/Projects/skills/.gitignore` if needed for cleanup
- Optional: remove dependence on `/Users/koohyomin/.claude/skills/research-first/SKILL.md` by copying its contents into the repo

# Open design choice
The only unresolved choice is what you mean by “index”:
- human-readable catalog in `README.md` only, or
- additional machine-readable file (JSON/YAML) for your own tooling

Because no verified skills.sh registry manifest was found, the recommended default is `README.md` only unless you specifically want an extra local metadata file.

# Verification
- Confirm the repo contains `skills/<skill-name>/SKILL.md`.
- Confirm `SKILL.md` still has valid frontmatter (`name`, `description`).
- Validate install examples in docs style:
  - `npx skills add <owner/repo>`
  - `npx skills add <owner/repo> --skill research-first`
- If more skills are added later, confirm each lives under `skills/<name>/SKILL.md` and appears in the repo index.
- Optionally test with the real CLI after the repo is pushed to GitHub.