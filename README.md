<div align="center">

<h1>de-ai-writing</h1>

<p><strong>A bilingual Codex skill for making Chinese and English writing sound natural, specific, and authorial—without changing the evidence.</strong></p>

<p>
  <a href="README.zh-CN.md">简体中文</a>
  ·
  <a href="https://github.com/qiyanghong2020/de-ai-writing/issues">Issues</a>
  ·
  <a href="#installation">Install</a>
</p>

<p>
  <a href="https://github.com/qiyanghong2020/de-ai-writing/stargazers"><img src="https://img.shields.io/github/stars/qiyanghong2020/de-ai-writing?style=social" alt="GitHub stars"></a>
  <a href="https://github.com/qiyanghong2020/de-ai-writing/commits/main"><img src="https://img.shields.io/github/last-commit/qiyanghong2020/de-ai-writing" alt="Last commit"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/qiyanghong2020/de-ai-writing" alt="MIT License"></a>
  <img src="https://img.shields.io/badge/Codex-skill-111827" alt="Codex skill">
  <img src="https://img.shields.io/badge/languages-English%20%7C%20中文-2563EB" alt="English and Chinese">
</p>

</div>

`de-ai-writing` is a Codex skill for revising prose that feels over-structured, generic, repetitive, translation-shaped, or machine-smoothed. It works across Chinese and English academic writing, medical manuscripts, theses, emails, application materials, reports, product documents, and long-form conceptual papers.

This is not an AI-detector bypass or a synonym spinner. The skill preserves factual claims, numbers, citations, uncertainty, genre, and author intent while fixing the patterns that make otherwise correct writing feel templated.

## What it catches

- stock transitions and over-explained scaffolding
- repeated sentence frames, symmetrical rhetoric, and uniform rhythm
- abstract claims with no clear subject, action, condition, or consequence
- flattened author voice and translation-like English or Chinese
- academic language that sounds polished but exceeds the evidence
- cross-section repetition in long manuscripts
- decorative taxonomies and repeated labels that add no analytical function
- structure-sensitive problems in long Word or document workflows

## Before and after

### English

> **Before:** Importantly, it is worth noting that self-verification plays a crucial role in enhancing trustworthiness; however, it cannot fully replace external validation.

> **After:** Self-verification can catch internal inconsistencies, but it does not establish external validity.

### 中文

> **修改前：** 值得注意的是，该结果进一步凸显了在实际应用场景中持续优化相关机制的重要性。

> **修改后：** 该结果说明，相关机制在实际应用前仍需继续优化。

The goal is not to make writing casual or imperfect. It is to remove verbal padding while keeping the original claim and evidence boundary intact.

## Installation

### Install with Codex

Ask Codex:

```text
Use $skill-installer to install the skill from https://github.com/qiyanghong2020/de-ai-writing.
```

The skill becomes available on the next Codex turn.

### Manual installation

On macOS or Linux:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/qiyanghong2020/de-ai-writing.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/de-ai-writing"
```

If a directory with that name already exists, review or update it instead of overwriting it.

## Usage

Invoke the skill explicitly with `$de-ai-writing`.

### General rewrite

```text
Use $de-ai-writing to rewrite this draft so it sounds natural and specific while preserving every fact, citation, number, and limitation.
```

### Chinese academic or medical writing

```text
Use $de-ai-writing to revise this Chinese discussion section. Remove translation-shaped abstractions and formulaic transitions, but keep the evidence level and medical terminology unchanged.
```

### English manuscript editing

```text
Use $de-ai-writing to edit this English manuscript paragraph for natural academic English. Preserve the author's World English register and do not strengthen the claims.
```

### Long Viewpoint or framework paper

```text
Use $de-ai-writing to audit this full Viewpoint before rewriting. Map where the central thesis recurs, inventory gates/states/tiers/frameworks, identify sections with low analytical increment, and propose compression without deleting necessary Methods, Results, definitions, limitations, or Introduction–Conclusion correspondence.
```

## Long-manuscript structural audit

Local sentence cleanup is not enough when the AI tone sits in the architecture of a paper. For authorized whole-manuscript work, the skill can:

1. summarize the central thesis in one sentence;
2. build a thesis-recurrence map across sections;
3. check whether each recurrence adds evidence, a qualification, a counterargument, an operational consequence, or a new inference;
4. inventory repeated labels such as `framework`, `boundary`, `gate`, `tier`, `state`, `class`, `level`, `matrix`, and `model`;
5. assign each section one distinct job;
6. compress low-increment repetition before local rewriting.

It does not mechanically delete taxonomies or normal Introduction–Conclusion echoes. A framework stays when its categories change interpretation, evaluation, decisions, or action.

## Design principles

- **Meaning first.** Facts, citations, numbers, comparison direction, limitations, and uncertainty are protected.
- **Genre matters.** A medical Discussion, a product README, and an email should not share one generic “human” voice.
- **Chinese and English are separate lanes.** The skill does not force English writing habits onto Chinese prose.
- **Specificity beats randomness.** It does not add typos, slang, anecdotes, or invented examples to imitate a person.
- **No detector promises.** Style signals cannot reliably prove authorship, and detector scores are not the optimization target.
- **Scope stays authorized.** A request for one paragraph does not become an unsolicited rewrite of the full manuscript.

## Repository structure

```text
de-ai-writing/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── references/
    ├── chinese.md
    ├── english.md
    ├── execution-patterns.md
    ├── markers.md
    ├── rewrite_patterns.md
    ├── risk_words_quicklist.md
    └── thesis-medical.md
```

`SKILL.md` contains the routing and core safeguards. Detailed language patterns and long-document workflows live in the references so the skill can load only what the current task needs.

## Limits

- Final prose style cannot establish whether a passage was written by a person or a model.
- AI-detector output is not treated as conclusive evidence.
- Disclosure questions should be assessed from the actual workflow and the target journal or institution's policy.
- The user remains responsible for verifying revised text before submission or publication.

## License

Released under the [MIT License](LICENSE).

## Contributing

Issues and pull requests are welcome. Especially useful contributions include:

- Chinese or English examples where the facts remain unchanged but the prose becomes more natural;
- field-specific false positives in academic, medical, technical, or professional writing;
- cases where a legitimate taxonomy or necessary repetition should be preserved;
- reproducible long-document edge cases.

Please do not submit rules whose only goal is to manipulate an AI-detector score.

---

If this skill helps you keep the substance while losing the template, consider [starring the repository](https://github.com/qiyanghong2020/de-ai-writing).
