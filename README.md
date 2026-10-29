# Vulgar Skill

A lightweight, Markdown-only Agent Skill for writing technically accurate Git commit messages with natural profanity in English or regional Spanish. It prioritizes meaning, language consistency, grammar, and Conventional Commits; profanity adds voice only when it fits.

> **Explicit language:** this Skill uses uncensored ordinary profanity. Generated messages may be inappropriate for professional, public, or customer-facing repositories. Review before use.

## Features

- Root-level Agent Skill for skills.sh and compatible coding agents.
- English-only or Spanish-only descriptions by default; Spanglish only when explicitly requested.
- Regional vocabulary from 20 Spanish-speaking countries and American, British, Australian, and international English.
- Context-aware expressions organized by meaning and grammatical use.
- Conventional Commit types, scopes, breaking-change markers, and footers.
- Variety guided by conversation and optional recent Git history.
- No scripts, dependencies, hooks, databases, or runtime setup.

## Installation

```bash
npx skills add Angel11R99/vulgar-skill
npx skills add Angel11R99/vulgar-skill -g
```

For agent-specific installation, use the CLI's supported selector, for example `npx skills add Angel11R99/vulgar-skill -a codex`. CLI options and supported agent identifiers can change; consult `npx skills add --help`.

## Usage

Ask a compatible agent to draft a commit message for the staged changes. The Skill identifies the real action, chooses the language, writes a clear message, and adds fitting profanity only if it remains natural. You can specify a language or region, such as “Use Mexican Spanish” or “Use British English.” When you provide a message, it will be improved in that message's language.

```text
fix(blog): agregadas las malditas imágenes que faltaban
fix(blog): finally added the damn missing images
```

Those subjects describe adding missing image files. They do not claim that upload behavior was fixed. See [50+ manually reviewed examples](references/commit-examples.md), the [Spanish catalog](references/spanish-profanity.md), and the [English catalog](references/english-profanity.md).

## Contributing

Keep expressions authentic to their region, add usage notes for ambiguous terms, and preserve the meaning of each example. Keep the project lightweight and Markdown-only; do not add scripts, dependencies, hooks, or generated catalogs.

## License

MIT; see [LICENSE](LICENSE).
