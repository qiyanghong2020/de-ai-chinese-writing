<div align="center">

# de-ai-writing

**A bilingual academic humanizer for Chinese and English manuscripts.**

**Preserve the evidence. Audit the whole argument.**

[简体中文](README.zh-CN.md) · [Examples](examples/README.md) · [Install](docs/installation.md) · [Privacy](docs/privacy.md) · [Terms](docs/terms.md) · [Issues](https://github.com/qiyanghong2020/de-ai-writing/issues)

[![GitHub stars](https://img.shields.io/github/stars/qiyanghong2020/de-ai-writing?style=social)](https://github.com/qiyanghong2020/de-ai-writing/stargazers)
[![Release](https://img.shields.io/github/v/release/qiyanghong2020/de-ai-writing?display_name=tag)](https://github.com/qiyanghong2020/de-ai-writing/releases)
[![Validate](https://github.com/qiyanghong2020/de-ai-writing/actions/workflows/validate.yml/badge.svg)](https://github.com/qiyanghong2020/de-ai-writing/actions/workflows/validate.yml)
[![skills.sh](https://skills.sh/b/qiyanghong2020/de-ai-writing)](https://skills.sh/qiyanghong2020/de-ai-writing)
[![MIT License](https://img.shields.io/github/license/qiyanghong2020/de-ai-writing)](LICENSE)

</div>

`de-ai-writing` helps humanize AI writing without flattening the author's work. It edits Chinese writing, English manuscripts, medical writing, emails, applications, and technical documents while protecting facts, numbers, citations, comparison direction, evidence strength, uncertainty, and the writer's register.

For an authorized full-paper review, it also runs a long-form structural audit: it maps cross-section thesis recurrence, identifies conceptual relabeling and decorative taxonomies, and tests whether manuscript length is proportionate to the evidence and analytical contribution.

It is not a synonym spinner, an AI-authorship test, or a detector-bypass tool.

## Quick start

Install with the open-source `skills` CLI:

```bash
npx skills add qiyanghong2020/de-ai-writing -g
```

Or install for Codex, Claude Code, and Cursor in one command:

```bash
npx skills add qiyanghong2020/de-ai-writing \
  -g -a codex -a claude-code -a cursor -y
```

Claude Code users can also install the repository as a plugin:

```text
/plugin marketplace add qiyanghong2020/de-ai-writing
/plugin install de-ai-writing@de-ai-writing
/reload-plugins
```

Reload the plugins to activate the skill in the current session, or restart Claude Code.

See the [cross-agent installation guide](docs/installation.md) for manual paths, project-level installs, updates, and invocation details.

## Shared baseline

A trustworthy writing skill should preserve meaning, avoid invented detail, match the writer's voice, diagnose patterns in context, and never treat prose style as proof of AI authorship. `de-ai-writing` starts from that baseline.

## What de-ai-writing adds

| Additional layer | What changes in practice |
| --- | --- |
| Chinese and English lanes | Loads language-specific guidance instead of forcing both languages through one style |
| Academic and medical safeguards | Protects evidence strength, statistics, causal limits, field terms, and manuscript subgenres |
| World English preservation | Improves clarity without replacing a legitimate local or non-native register with generic corporate English |
| Document-level thesis mapping | Tracks the same proposition across sections, not only repeated words in adjacent paragraphs |
| Framework and terminology inventory | Merges labels only when they rename the same concept without changing interpretation or action |
| Taxonomy false-positive protection | Keeps categories whose evidence, decisions, or permissible claims differ |
| Contribution-to-length audit | Compresses low-increment repetition without mechanically pursuing the shortest text |
| Authorship and disclosure boundaries | Separates style diagnosis from claims about who wrote the text or whether disclosure is sufficient |

## See the workflow

<div align="center">
<img src="assets/social-preview.png" alt="de-ai-writing — Natural Chinese and English writing. Keep the evidence. Lose the template." width="100%">
</div>

<div align="center">
<img src="assets/demo.gif" alt="Thirty-second illustrated workflow: lock evidence, diagnose repetition, rewrite, and audit long papers" width="900">
</div>

The demo uses synthetic material. No manuscript was uploaded to produce it.

## Use it

### General rewrite

```text
Use de-ai-writing to revise this draft so it sounds natural and specific while preserving every fact, citation, number, and limitation.
```

### Chinese medical or academic writing

```text
请使用 de-ai-writing 修改这段中文讨论。减少翻译腔、抽象套话和模板化连接词，但不要改变证据强度、统计量和医学术语。
```

### English manuscript editing

```text
Use de-ai-writing to edit this manuscript paragraph for natural academic English. Preserve the author's World English register and do not strengthen the claims.
```

### Long Viewpoint or framework paper

```text
Use de-ai-writing to audit this full Viewpoint before rewriting. Map where the central thesis recurs, inventory gates/states/tiers/frameworks, identify sections with low analytical increment, and propose compression without deleting necessary Methods, Results, definitions, limitations, or Introduction–Conclusion correspondence.
```

Invoke a plain skill install as `$de-ai-writing` in Codex or `/de-ai-writing` in Claude Code and Cursor. A Claude Code plugin install uses `/de-ai-writing:de-ai-writing`. Automatic discovery can also apply the skill when the request matches its description.

## Worked examples

All examples are synthetic and show the protected facts, diagnosis, revision, and deliberate non-edits.

| Example | Decision demonstrated |
| --- | --- |
| [English academic paragraph](examples/01-english-academic.md) | Keeps an observational association below the causal ceiling |
| [English workplace email](examples/02-english-email.md) | Makes the ask and deadline visible without becoming abrupt |
| [Chinese medical discussion](examples/03-chinese-medical.md) | Preserves sample size, effect estimate, interval, and design limit |
| [Chinese workplace email](examples/04-chinese-workplace-email.md) | Removes procedural padding while keeping professional respect |
| [30-page Viewpoint audit](examples/05-viewpoint-structural-audit.md) | Maps thesis recurrence and merges decorative concept labels |
| [Taxonomy negative control](examples/06-taxonomy-preservation.md) | Retains categories with independent decision consequences |
| [World English preservation](examples/07-world-english.md) | Improves clarity without erasing a setting-specific register |

### Two structural decisions at a glance

**A repetitive 30-page Viewpoint.** The same clinical-validity thesis appears in the Abstract, Introduction, limits, gates, evidence states, governance, and Conclusion. The audit keeps the necessary opening and closing correspondence, retains the two gates because they change the evaluation sequence, removes a duplicate state layer, and merges two overlapping governance taxonomies. [See the recurrence map and compression plan.](examples/05-viewpoint-structural-audit.md)

**A neat taxonomy that should stay.** Technical, retrospective clinical, and prospective clinical states each permit a different next action and a different claim. The skill keeps all three and removes only a final sentence that repeats their names without adding a consequence. [See the negative control.](examples/06-taxonomy-preservation.md)

## How it works

1. **Lock meaning.** Protect claims, figures, sources, comparison direction, and uncertainty.
2. **Choose the lane.** Use Chinese, English, medical/thesis, or long-document guidance only when relevant.
3. **Diagnose before rewriting.** Identify whether the problem is lexical, structural, tonal, evidentiary, or a loss of author voice.
4. **Rewrite at the right scale.** Edit the local block, or—when authorized—compress document-level repetition before line editing.
5. **Run the human pass.** Check that the result is plausible for the genre and has not invented detail or strengthened a claim.

Detailed rules stay in `references/` so agents load them progressively instead of placing a large tutorial in `SKILL.md`.

## Long-manuscript structural audit

For an authorized full-paper edit, the skill can:

- summarize the central thesis in one sentence;
- build a thesis-recurrence map across sections;
- test whether each recurrence adds evidence, a qualification, a counterargument, an operational consequence, a new inference, or a failure boundary;
- inventory labels such as `framework`, `boundary`, `gate`, `tier`, `state`, `class`, `level`, `matrix`, and `model`;
- give each section one distinct job;
- compress low-increment repetition before sentence-level polishing.

It does not mechanically delete taxonomies, definitions, Methods, Results, limitations, or normal Abstract–Introduction–Conclusion correspondence. See the [complete Viewpoint example](examples/05-viewpoint-structural-audit.md) and the [taxonomy preservation case](examples/06-taxonomy-preservation.md).

## Privacy

This repository is a local set of instructions and references. It does not host a rewriting service or collect manuscript text. The agent and model you choose may process your text under their own policies.

Do not paste unpublished manuscripts, patient identifiers, confidential peer review, credentials, or legally sensitive text into an unreviewed third-party demo. A hosted demo should be linked only after its operator, model subprocessors, retention, training use, deletion route, and incident responsibility are documented. Read the [privacy guidance](docs/privacy.md).

## What is actually tested

Run the repository contract tests:

```bash
python3 -m unittest discover -s tests -v
```

Inspect portable Agent Skills discovery without installing:

```bash
npx skills add . --list
```

The repository distinguishes three levels of evidence:

- **Repository contract tests** check frontmatter, version consistency, reference paths, safeguards, plugin manifests, example coverage, local links, and fixture structure.
- **Behavior/evaluation fixtures** specify protected claims, expected decisions, forbidden outcomes, and result shapes for synthetic cases. They are reusable inputs for manual or future automated forward tests.
- **Model end-to-end evaluation has not been run by these tests.** Passing the suite does not prove that every Agent or model will produce a correct rewrite.

No test calls an AI detector, paid API, or external rewriting service, and no test modifies a user document. See the [evaluation specification](evals/README.md).

## Repository map

```text
de-ai-writing/
├── .claude-plugin/          # Claude Code plugin and marketplace metadata
├── SKILL.md                 # routing and core safeguards
├── references/              # Chinese, English, medical, and long-document guidance
├── examples/                # seven complete worked cases
├── evals/                   # synthetic behavior fixtures; not model results
├── tests/                   # deterministic repository contract tests
├── docs/                    # installation and privacy guidance
├── assets/                  # social preview and illustrated demo
└── agents/openai.yaml       # Codex interface metadata
```

## Boundaries

- Final prose style cannot establish whether a person or model wrote a passage.
- AI-detector output is not conclusive evidence.
- Disclosure questions must be assessed from the actual workflow and the target journal or institution's policy.
- A paragraph-level request does not authorize an unsolicited full-manuscript restructure.
- Users remain responsible for verifying revised text before submission or publication.

## Contributing

Issues and pull requests are welcome, especially for:

- **False positives:** a legitimate phrase, taxonomy, quotation, or necessary repetition that the skill removed. Include the genre, source excerpt, expected decision, and actual result.
- **Meaning loss:** a rewrite that dropped or changed a fact, ranking, simultaneity claim, effect direction, uncertainty, limitation, citation relationship, or scope boundary.
- **Long-document cases:** reproducible cross-section repetition, conceptual relabeling, decorative frameworks, or contribution-to-length problems. Use synthetic or publishable material and identify which sections should perform distinct jobs.

Do not submit rules whose only goal is to manipulate an AI-detector score. See the [design provenance](UPSTREAM.md) for earlier influences and rejected tactics.

## License

Released under the [MIT License](LICENSE).

---

If this skill helps you keep the substance while losing the template, [star the repository](https://github.com/qiyanghong2020/de-ai-writing) and share one example that challenged it.
