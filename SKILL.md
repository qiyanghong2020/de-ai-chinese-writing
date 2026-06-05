---
name: de-ai-writing
description: Rewrite Chinese or English prose so it reads more naturally and less like AI-generated text while preserving facts, evidence, logic, genre, and author intent. Use when the user asks to 去 AI 腔, 去除 AI 味, humanize writing, make it less AI, less ChatGPT-like, less generic, more natural, more human, more authorial, less templated, or when Chinese or English prose feels over-structured, repetitive, connector-heavy, vague, over-polished, lexically flat, voice-less, translation-like, or machine-smoothed. Works across English manuscripts, academic writing, thesis prose, Chinese medical writing, translated drafts, emails, application letters, reports, PRDs, README files, product copy, presentations, newsletters, and other Chinese or English writing tasks.
---

# De-AI Writing

Use this skill to turn stiff, templated, or machine-smoothed Chinese or English into natural human prose without flattening the substance, faking personality, or chasing detector scores.

## Choose the language lane

Load only the references that fit the task:

- Read `references/chinese.md` for Chinese drafts or mixed drafts where the main prose is Chinese.
- Read `references/english.md` for English drafts or mixed drafts where the main prose is English, especially academic manuscripts, section-level manuscript editing, translation-like English, sentence polishing, emails, application letters, narrative prose, or requests that mention tools such as Paperpal, DeepL Write, Grammarly, Wordtune, Hemingway Editor, ProWritingAid, QuillBot, or "AI humanizer".
- Read `references/execution-patterns.md` for long documents, layout-sensitive documents, staged rewrites, or files with automatic fields.
- Read `references/thesis-medical.md` for Chinese theses, dissertations, medical papers, academic discussion sections, or formal Chinese scholarly prose.

For Chinese work, use `references/chinese.md` first; it points to `references/markers.md`, `references/rewrite_patterns.md`, and `references/risk_words_quicklist.md` when concrete examples or quick phrase checks are needed.

For English work, use `references/english.md` first; it contains the English-specific AI-tone markers, phrase risks, and genre lanes.

For English biomedical manuscripts or English tables in medical papers, keep the work in the English lane and use `references/english.md`, especially the scientific/medical table-language guidance. Use `references/thesis-medical.md` only when the main prose is Chinese medical or formal Chinese scholarly writing.

## Core workflow

### 1. Lock the meaning

Before rewriting, preserve:

- factual claims
- source role or document purpose
- sample size, dates, numbers, and named entities
- effect direction and comparison structure
- evidence boundary, limitation, uncertainty, or scope
- citation relationship and attribution

Do not add examples, anecdotes, data, citations, author emotions, dialect markers, or first-person claims unless they are already present or the user explicitly asks for them.

### 2. Diagnose before rewriting

Make a quick local diagnosis:

- Which language lane applies?
- What genre is this: academic, public article, report, product doc, email, speech, personal essay, or README?
- Which edit lens applies: academic manuscript, naturalized translation, tone and clarity, expression variants, brevity, long-form style, or humanizer-caution?
- Is the AI feel mostly lexical, structural, tonal, or caused by missing specificity?
- Does the user provide a writing sample that should calibrate rhythm and stance?
- Are there protected zones: references, formulas, tables, citations, figure titles, legal wording, automatic fields, code, or UI strings?

### 3. Rewrite the whole local block

AI tone usually appears in clusters. If the user points to one awkward sentence, inspect and rewrite the local block, not only the quoted sentence.

At minimum, check:

- the quoted sentence
- the paragraph it sits in
- the paragraph before and after when available
- any heading, caption, summary box, or bullet list that carries the same tone

For long or structure-sensitive documents, use paragraph or local block as the default unit. Skip short structural labels unless the user explicitly wants them rewritten.

### 4. Calibrate to the writer

If the user provides a sample of their own writing, extract a compact style memory:

- sentence length tendency: short, medium, or long
- paragraph opening habit: direct entry, contextual setup, or mixed
- punctuation habit
- stance level: flat explanatory, mildly assertive, personal, formal, or visibly authorial
- register: academic, business, technical, public-facing, conversational, or local English variety

Apply rhythm and stance without copying verbal tics mechanically. Preserve a writer's legitimate Chinese style, non-native English style, or World English variety when it carries identity or pragmatic meaning.

### 5. Remove machine polish first

Prioritize fixes that restore specific human judgment:

- replace vague abstractions with concrete subjects, verbs, conditions, and outcomes
- reduce stock transitions when the relation is already clear
- break repeated sentence skeletons and paragraph openings
- vary sentence pressure according to meaning, not for cosmetic irregularity
- cut meta-commentary about the writing itself
- remove teacher-like reader management and over-helpful scaffolding
- replace generic enthusiasm with evidence, constraint, consequence, or choice
- preserve field-typical terms when they are precise

Do not make the prose longer just to seem more human. Do not introduce mistakes, slang, or awkwardness as camouflage.

If the request is framed around a direct "AI humanizer" or detector bypass tool, convert it into a meaning-preserving genre edit. Avoid synonym churn, random imperfection, and any promise that the output will evade Turnitin, GPTZero, or another detector.

### 6. Match the genre

Academic and thesis writing:

- keep evidence-reporting verbs and field-typical nouns
- distinguish exploratory findings from confirmed conclusions
- avoid adding first person unless the genre or user allows it
- keep citations, methods, results, and limitations conservative

Reports, PRDs, READMEs, and technical docs:

- name the owner, object, action, constraint, and result
- prefer measurable or observable wording over strategy fog
- keep commands, API names, UI labels, and code terms exact

Public articles, newsletters, and explainers:

- speak directly to the topic, not to the act of reading
- keep the reader relationship flat and respectful
- add warmth only where the genre already allows it

Emails and workplace messages:

- make the ask, context, deadline, and next step clear
- avoid corporate padding and over-politeness
- keep tone appropriate to the relationship

### 7. Final human pass

Before output, check:

- meaning and evidence boundaries are unchanged
- no invented facts, citations, examples, or personal details
- no detector-evasion claim or promise
- the rewrite sounds like a plausible person in that genre
- the paragraph no longer depends on stock phrasing to feel organized
- any retained high-risk words are there because they are precise

When returning a rewrite, output the rewritten content directly unless the user asks for explanation, diagnostics, or before/after notes.
