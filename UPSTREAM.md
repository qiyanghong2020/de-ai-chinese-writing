# Upstream Notes

## Source

- upstream repo: `https://github.com/qiyanghong2020/de-ai-chinese-writing.git`
- local active skill path: `/home/hongqy/.codex/skills/de-ai-chinese-writing`
- current branch: `main`

## Local organization

This local skill is now arranged as an upstream-based working tree:

- tracked upstream files come from the GitHub repository
- local changes stay as normal git modifications on top of upstream
- local-only additions stay as untracked or newly added files until intentionally committed

## Local additions kept on top of upstream

- stronger academic / thesis / medical guidance
- explicit checks for transition-word overload such as `此外` / `然而` / `总之`
- explicit checks for overly uniform grammar and sentence landing
- extra quick references for phrase-level rewrites and risk words
- local reference file: `references/thesis-medical.md`

## Practical sync workflow

To review upstream changes later:

```bash
git -C /home/hongqy/.codex/skills/de-ai-chinese-writing fetch origin
git -C /home/hongqy/.codex/skills/de-ai-chinese-writing diff --stat HEAD origin/main
git -C /home/hongqy/.codex/skills/de-ai-chinese-writing diff HEAD origin/main
```

To see only local edits on top of upstream:

```bash
git -C /home/hongqy/.codex/skills/de-ai-chinese-writing status --short
git -C /home/hongqy/.codex/skills/de-ai-chinese-writing diff
```

## Reminder

The active skill is the local directory under `~/.codex/skills`, not the remote repository by itself.
