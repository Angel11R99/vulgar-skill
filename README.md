# Vulgar Skill

Generate technically accurate Conventional Commit messages with multilingual English and regional Spanish profanity, intelligent variation, and configurable intensity.

This Agent Skill is intentionally vulgar. It favors multiple swear words per message at medium and high intensity while keeping the actual code change clear. Profanity targets frustrating code or behavior, never people or protected groups.

## Install

Replace `OWNER` with the public GitHub username or organization that publishes this repository:

```sh
npx skills add OWNER/vulgar-skill
npx skills add OWNER/vulgar-skill -a codex
npx skills add OWNER/vulgar-skill -g
```

Local discovery and installation from the repository root:

```sh
npx skills add ./ --list
npx skills add ./
```

The skills CLI installs the skill for compatible agents. Check its current help for supported agent identifiers and global install behavior. A public GitHub repo and successful install do not guarantee immediate indexing or ranking on skills.sh. Remote install has not been tested unless a maintainer records that validation here.

## Compatible agents

Designed for Agent Skills-compatible coding agents, including OpenAI Codex, Claude Code, Cursor, OpenCode, and GitHub Copilot coding agents. Install through `npx skills` where supported. Optional agent integration can reference this skill from that agent's project instructions; no `AGENTS.md`, `CLAUDE.md`, machine path, hook, or global Git setting is required.

## Coverage and behavior

- English: American, British, Australian.
- Spanish: Dominican, Mexican, Spanish, Argentine, Colombian, Venezuelan, and broader regional expressions.
- Conventional Commits types, scopes, breaking change markers, and footers.
- Default/high intensity uses two or more profanity terms; medium uses two moderate terms; low uses one mild term. Ask for clean output to disable profanity.
- Language and locale rotate when no preference is given. The skill respects explicit language and avoids repeating recent phrasing when history is available.
- It reads the actual diff before describing technical changes. Scripts are optional and standard-library only.

### Intensity

Choose `low`, `medium`, or `high` in your request. Low keeps the message mildly irreverent. Medium uses two moderate terms. High is brutally vulgar with multiple strong terms. The technical description always remains accurate and readable.

### Agent integration

The same skill directory works across compatible agents. Install for one agent with `npx skills add OWNER/vulgar-skill -a claude-code` (replace the agent identifier with one shown by the CLI). Alternatively, use each agent's standard skills directory or have an existing project instruction file reference the installed `SKILL.md`. No agent-specific wrapper is needed.

## Examples

See [examples/commits.md](examples/commits.md) for 30 example messages. Catalog term counts are computed from the JSON catalogs; use `python scripts/validate_catalog.py` to print them. Counts are not advertised here as hand-verified statistics.

## Validation

Python 3.8+ is optional. No third-party packages are required.

```sh
python scripts/validate_catalog.py
python -m unittest discover -s tests -v
python scripts/validate_commit.py "fix(auth): stop the damn token refresh loop"
```

The generator takes a technical description and optional Conventional Commit type/scope, language, region, intensity, and previous message arguments. See `python scripts/generate_commit.py --help`.

## Contributing

Open an issue or pull request with focused changes. Catalog entries should be genuine, locally used expressions with a language and region specified. Explain regional nuance and avoid slurs, threats, or identity-based insults. Keep technical documentation in English, data UTF-8, dependencies optional, and tests deterministic. Validate JSON, scripts, and relative links before submitting.

## Disclaimer

Generated commit messages may be inappropriate for professional, corporate, public, or customer-facing repositories. Review every message before using it.

## License

MIT. See [LICENSE](LICENSE).
