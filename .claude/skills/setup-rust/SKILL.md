---
name: setup-rust
description: Set up Claude Code hooks for Rust projects when a Cargo.toml file exists. Use when the user wants Rust quality checks wired into settings.json/settings.local.json, asks to enable cargo check/fmt/clippy hooks, or wants automatic Rust validation for a repository.
---

Check whether the repository contains any `Cargo.toml` file before changing settings. If none exists, report that no Rust project was detected and do not add Rust hooks.

When a `Cargo.toml` exists, configure Claude Code hooks in the project settings so Rust commands run automatically without blocking the main action.

Prefer editing `.claude/settings.json` in the repository. If the repository already uses `.claude/settings.local.json` for local-only automation, follow the existing pattern instead of introducing a second settings file.

Add Rust commands as non-blocking shell hooks by appending `|| true` to each command:

- `cargo check || true`
- `cargo fmt --all || true`
- `cargo clippy --all-targets --all-features -- -D warnings || true`

Use `cargo fmt --all`, not plain `cargo fmt`.
Use `cargo clippy --all-targets --all-features -- -D warnings`, not a shorter variant.

If the settings file already contains hooks, merge the Rust hooks into the existing structure instead of replacing unrelated entries. Avoid duplicate Rust hook commands.

After editing settings, read the final file back and verify that all three Rust commands are present exactly once with the required flags.
