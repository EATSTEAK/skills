---
name: use-pnpm
description: Always use pnpm/pnpx for Node.js work unless the project packageManager field specifies another package manager. Use when Node.js, JavaScript, TypeScript, npm scripts, package installation, or Node CLI tools are involved.
---

Prefer the package manager declared in the nearest `package.json` `packageManager` field.
If no `packageManager` field is present, use `pnpm` and `pnpx` for all Node-related commands.

Do not call `npm`, `npx`, `yarn`, `yarn dlx`, `bun`, or `bunx` unless the nearest `package.json` explicitly declares that package manager or the user explicitly asks.
Run package scripts with `pnpm <script>` or `pnpm run <script>`.
Install dependencies with `pnpm add <package>` and development dependencies with `pnpm add -D <package>`.
Remove dependencies with `pnpm remove <package>`.
Install and align dependencies with `pnpm install`.
Run project-local CLIs with `pnpm exec <tool>`.
Run one-off external Node CLIs with `pnpx <tool>` when you do not need to modify the project.

Before choosing a Node package manager, check the nearest `package.json` for `packageManager` when it is not already known from context.
