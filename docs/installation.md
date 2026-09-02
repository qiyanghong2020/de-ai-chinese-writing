# Installation across Agent Skills clients

`de-ai-writing` follows the open [Agent Skills specification](https://agentskills.io/specification). Its root `SKILL.md` uses only portable fields and relative reference paths.

## One command for Codex, Claude Code, and Cursor

The open-source `skills` CLI can install the same checkout for all three agents:

```bash
npx skills add qiyanghong2020/de-ai-writing \
  -g -a codex -a claude-code -a cursor -y
```

Remove `-g` for a project-level installation. Without `-y`, the CLI lets you review the skill and installation method interactively.

To inspect the repository without installing it:

```bash
npx skills add qiyanghong2020/de-ai-writing --list
```

## Codex

Ask Codex to install the repository:

```text
Use $skill-installer to install https://github.com/qiyanghong2020/de-ai-writing.
```

For a manual global installation:

```bash
git clone https://github.com/qiyanghong2020/de-ai-writing.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/de-ai-writing"
```

Invoke it with `$de-ai-writing`, or describe a matching Chinese or English editing task and allow normal skill discovery.

## Claude Code

For a versioned, repository-backed plugin install:

```text
/plugin marketplace add qiyanghong2020/de-ai-writing
/plugin install de-ai-writing@de-ai-writing
/reload-plugins
```

Reloading activates the plugin in the current session; restarting Claude Code also applies the change. The plugin keeps the root `SKILL.md` as the single skill entry point and packages its relative references with the repository. Invoke the installed plugin as `/de-ai-writing:de-ai-writing`.

For a plain personal-skill install without plugin namespacing, Claude Code discovers personal skills under `~/.claude/skills/` and project skills under `.claude/skills/`:

```bash
git clone https://github.com/qiyanghong2020/de-ai-writing.git \
  "$HOME/.claude/skills/de-ai-writing"
```

Invoke a plain skill install with `/de-ai-writing`. Claude Code can also load it automatically when the request matches the frontmatter description.

## Cursor

Cursor discovers user skills under `~/.cursor/skills/` or `~/.agents/skills/`, and project skills under `.cursor/skills/` or `.agents/skills/`.

```bash
git clone https://github.com/qiyanghong2020/de-ai-writing.git \
  "$HOME/.cursor/skills/de-ai-writing"
```

Open the `/` menu in Agent chat and select `de-ai-writing`. Cursor also supports importing a remote GitHub skill from **Customize → Rules → Add Rule → Remote Rule (GitHub)**.

## Other Agent Skills clients

Use the client-neutral project path when your agent supports the open convention:

```text
.agents/skills/de-ai-writing/SKILL.md
```

The repository root is the skill folder. Keep `SKILL.md`, `references/`, and `agents/` together so relative paths continue to resolve.

## Updating

If installed with the `skills` CLI:

```bash
npx skills update de-ai-writing -g -y
```

If cloned manually:

```bash
git -C /path/to/de-ai-writing pull --ff-only
```

Do not overwrite a modified local copy. Review or commit local changes before updating.

## Verification

After installation, try one of the prompts in the main README or ask the agent to list available skills. A correct installation should expose the name `de-ai-writing` and load the relevant file under `references/` only when the task calls for it.

Official client references:

- [Agent Skills specification](https://agentskills.io/specification)
- [Claude Code skills](https://code.claude.com/docs/en/skills)
- [Claude Code plugins](https://code.claude.com/docs/en/plugins)
- [Claude Code plugin marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
- [Cursor Agent Skills](https://cursor.com/docs/skills)
- [`skills` CLI](https://github.com/vercel-labs/skills)
