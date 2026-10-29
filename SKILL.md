---
name: vulgar-skill
description: Write or review technically accurate Git commit messages with natural, context-aware profanity in English or regional Spanish. Use when drafting commit messages from changes or improving a supplied message while preserving Conventional Commits.
---

# Vulgar Skill

Write commit messages as a multilingual developer, not as a profanity generator. A message must make perfect technical and linguistic sense before profanity is added. Profanity is optional when it would make the sentence awkward; when used, it should sound native and fit the action and emotional context.

## Required workflow

1. Establish the evidence. Inspect staged changes first (`git diff --cached`), then relevant working changes or the user's description. Never expose secrets found in changes. If the user supplied a commit subject, preserve its actual claim while improving it.
2. State internally what changed, what action was performed, and whether it is complete. Distinguish adding files, uploading assets, changing existing assets, fixing upload behavior, deleting files, and optimizing them. Do not invent causes, outcomes, or frustration.
3. Select one language for the description, using this order: user's explicit language; explicit repository configuration; language of the user's supplied message; dominant language in recent, consistent relevant Git subjects; English fallback. Mixed recent history is not a preference. Keep the description in that language. Technical identifiers, filenames, names, Conventional Commit types, and established API terms keep their original spelling. Use Spanglish only on explicit request.
4. Choose the most accurate English Conventional Commit type: `feat`, `fix`, `refactor`, `perf`, `docs`, `test`, `build`, `ci`, `chore`, `style`, or `revert`. Add a truthful scope where useful. Preserve valid `!`, breaking-change markers, and footers.
5. Draft a concise, grammatical, technically precise message first, with a consistent tense and perspective. English can use the repository's established imperative style or a concise completed-change style; Spanish can use a natural completed-action form (for example, “se agregaron”, “se corrigió”, “eliminadas”, “optimizado”). Do not mix perspectives or tenses within a subject.
6. Choose profanity by grammatical role and context. Consult [Spanish profanity](references/spanish-profanity.md) or [English profanity](references/english-profanity.md). Use a regional expression only when that region is requested or clearly established. Do not translate idioms word for word. Aim profanity at software, behavior, or the situation, never a person. Avoid identity-based slurs, threats, and targeted harassment.
7. Integrate each expression as an exclamation, modifier, intensifier, frustrated conclusion, or coherent compound. One expression is often enough for a short subject. Use more only when the sentence supports them; never pad with disconnected swearing. Match tone to evidence: a fix may be frustrating or relieving, a feature celebratory, a refactor wry, a performance change satisfied, and docs/tests/infrastructure annoyed only when that tone is warranted.
8. Compare with recent relevant messages, if available, and vary expressions, openings, constructions, and tone without changing language or technical meaning. Do not create persistence systems.
9. Validate before returning: (a) accurate action and completion, (b) no invented detail, (c) one selected language, (d) native grammar and tense, (e) idiomatic and regionally appropriate profanity, (f) clear meaning, (g) valid Conventional Commits syntax and truthful footer, (h) no needless repetition. Rewrite if any check fails.
10. Return the message or use it in the requested workflow. Do not run `git commit` unless the user authorized committing. If evidence is unavailable, base the draft on the supplied facts and state material uncertainty.

## Format

`<type>(<scope>): <description>`

Types and scopes remain in their established form. Keep the description in one language. Examples:

```text
fix(auth): corregido el maldito error de autenticación
fix(auth): fixed the damn authentication bug
```

The Skill is instruction-only and Markdown-only: no scripts, runtime, hooks, dependencies, databases, or configuration are required.
