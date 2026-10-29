# Vulgar Skill

An instruction-based Agent Skill for generating technically accurate, funny, varied, profanity-heavy Git commit messages. It speaks English, regional Spanish, and Spanglish while preserving Conventional Commits.

> **Explicit language:** this Skill deliberately uses uncensored ordinary profanity. Generated messages may be inappropriate for professional, corporate, public, or customer-facing repositories. Review before use.

## Features

- Root-level Agent Skill for skills.sh and compatible coding agents.
- English-only, Spanish-only, and Spanglish messages.
- Regional vocabulary from 20 Spanish-speaking countries, plus American, British, Australian, and international English.
- Contextual humor and frustration, with one or multiple profanities as grammar allows.
- Conventional Commit types, scopes, breaking change markers, and footers.
- Anti-repetition informed by conversation context and optional recent Git history.
- No scripts, dependencies, hooks, databases, or runtime setup.

## Installation

Replace `OWNER` with the GitHub username or organization that publishes the repository:

```bash
npx skills add OWNER/vulgar-skill
npx skills add OWNER/vulgar-skill -g
```

For agent-specific installation, use the CLI's supported selector, for example `npx skills add OWNER/vulgar-skill -a codex`. CLI options and supported agent identifiers can change; consult `npx skills add --help`.

Installation makes the Skill available to a compatible agent; it does not automatically rewrite all manual Git commits. Ask the agent to draft a commit message, or explicitly invoke the Skill in an agent that supports explicit skills.

## Usage

Ask your compatible coding agent to generate a commit message for the staged changes. The Skill checks the actual diff, selects a fitting Conventional Commit type, describes the technical change, then adds an appropriate regional voice. You can specify a language or region, such as “Use Mexican Spanish” or “Make it Spanglish.”

Example:

```text
fix(auth): arreglar esta puta mierda del login
```

See [50+ examples](references/commit-examples.md) and the [Spanish](references/spanish-profanity.md) and [English](references/english-profanity.md) expression catalogs.

## Contributing

Contributions should use authentic expressions, preserve regional context, and avoid fabricating vocabulary to inflate counts. Include usage notes where meanings vary by country. Keep the project lightweight and Markdown-only; do not add scripts, dependencies, hooks, or generated catalogs.

## License

MIT; see [LICENSE](LICENSE).
