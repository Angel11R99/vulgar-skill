---
name: vulgar-skill
description: Generate multilingual, profanity-heavy Conventional Commit messages using authentic English and regional Spanish slang. Use when writing, suggesting, revising, or generating Git commit messages, including when an AI coding agent prepares a commit.
---

# Vulgar Skill

Generate technically accurate Git commit messages with deliberately strong, varied profanity. Keep the code change as the subject: profanity adds voice but must never obscure what changed.

Activate when asked to draft, rewrite, suggest, or prepare a commit message. Do not commit or alter repository state unless separately asked.

## Workflow

1. Inspect the actual staged diff first (`git diff --cached`); if none is staged, inspect the requested diff or working tree. Use status and filenames for context. Never infer changes from a request alone, include secrets, or claim behavior unsupported by the diff. If tool access is unavailable, ask for a diff or work in instruction-only mode from supplied details.
2. Choose the most accurate Conventional Commit type: `feat` for user-facing capability, `fix` for a defect, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, or `chore` as appropriate. Add a scope only when useful. Use `!` and a `BREAKING CHANGE:` footer only for actual incompatibility.
3. Write a concise imperative technical summary naming the affected behavior or component. Keep the subject readable and normally under 72 characters when practical. Put extra context in a body; do not let a profanity replace technical specificity.
4. Choose a catalog matching the user's requested language/region. Otherwise rotate English and Spanish and vary regions across commits. Regional slang is not interchangeable: honor explicit preferences, use only terms marked for the chosen locale, and avoid caricature. If unsure, use broad English or neutral Spanish.
5. At default/high intensity use at least two distinct profanity terms per commit, worked naturally into the subject/body. Low intensity uses one mild term; medium uses two moderate terms; high uses two or more strong terms. Keep slurs, threats, and identity-based abuse out. Never direct profanity at a person or group; target the bug, mess, or frustrating behavior. A user can request clean output or a lower intensity.
6. Avoid repetition: check recent messages if available, do not reuse the same opening, adjective pair, region, or language in consecutive outputs, and choose different catalog entries. Do not claim persistent history when none is available.
7. Validate the header grammar `<type>(optional-scope)!: description`, ensure the technical claim matches the diff, spelling and locale are natural, intensity is respected, and profanity count is sufficient. Use the optional validators when Python is available; otherwise follow these checks manually.

## Optional scripts

Scripts under `scripts/` are optional local helpers and use only the Python standard library. Run them from any current directory with paths to this repository's files. They only read inputs and print output; they do not install hooks, change Git settings, stage files, or commit. If Python is missing or execution is unavailable, use the workflow above without scripts. See `references/configuration.md` for options.
