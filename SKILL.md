---
name: de-ai-chinese-writing
description: Rewrite Chinese prose so it reads more naturally and less like AI-generated text while preserving facts, evidence, logic, and domain meaning. Use when the user asks to 去 AI 腔, make writing more human, more自然, more口语化但不油滑, less像教科书, less像模板, or when any Chinese draft feels over-structured, repetitive, connector-heavy, vague, or machine-smoothed. Works across articles, reports, PRDs, product copy, README files, presentations, newsletters, and other Chinese writing tasks.
---

# De-AI Chinese Writing

Use this skill to turn stiff, templated, or machine-smoothed Chinese into natural human prose without flattening the substance.

Read `references/markers.md` when you need concrete examples of AI-like phrasing patterns and preferred rewrites.
Read `references/rewrite_patterns.md` when you want phrase-level before/after rewrite patterns you can apply quickly.
Read `references/risk_words_quicklist.md` when you want a fast sweep for high-risk words and their more natural Chinese alternatives.

## Workflow

### 1. Keep meaning fixed

Before rewriting, lock these parts in place:

- factual claim
- source type or document role
- sample size or key numbers
- effect direction
- limitation, scope, or evidence boundary

Do not trade away domain meaning for a more casual tone.

### 2. Rewrite the whole local block, not just the quoted sentence

If the user points to one awkward sentence, inspect the surrounding paragraph and nearby section. AI tone usually appears in clusters.

At minimum, check:

- the quoted sentence
- the paragraph it sits in
- the paragraph before and after
- any heading or summary box that carries the same tone

### 3. Remove machine-smoothed wording first

Prioritize these fixes:

- replace vague “slippery” words with concrete subjects, actions, and outcomes
- replace translationese abstract nouns and source-language scaffolding with natural Chinese when a direct expression exists
- replace contrast framing such as `不是……而是……`, `并非……而是……`, `不只是……而是……`, and `不靠……而是……` with direct statements whenever precision does not require the contrast
- break over-smoothed rhythm when sentence length, sentence structure, or paragraph movement feels too even
- trim over-explained logic when the paragraph insists on spelling out every bridge instead of carrying one decisive point
- cut low-information connective openers
- remove rhetorical booster words and filler emphasis such as `真正`, `真正的`, `实际上`, `最值得`, or similar words when they are only propping up tone
- remove commentary about the writing itself
- remove reader-stage scaffolding and teacher-like prompts
- collapse textbook-style explanation scaffolding into direct content statements
- vary repeated sentence templates and paragraph openings
- clean up punctuation habits that make Chinese look machine-smoothed

Bad pattern:

- `这篇研究最值得记住的是……`
- `这更像是在提醒我们……`
- `结果落到……`
- `大面上……`

Preferred pattern:

- say it directly before you contrast it
- say what happened
- say what changed
- say what the number means
- say where the evidence stops

Recommended pass order:

1. remove commentary about the writing itself
2. replace contrast framing, rhetorical boosters, and teacher-like scaffolding with direct statements
3. replace滑词 and translationese abstract nouns
4. simplify绕行动词, nominalized phrasing, and over-standardized phrase bundles
5. break over-even rhythm and trim over-complete explanation
6. reduce repeated connectives and repeated “objective” openers
7. add a little human texture only if the paragraph still feels too flat

Pay special attention to these three common AI-polish symptoms:

- the sentences are too even in length, structure, and landing point
- every judgment is wrapped up too fully, leaving no natural white space
- abstract phrase bundles appear in clusters and start to feel like concept blocks rather than lived Chinese
- the paragraph logic falls into a standard review-style push every time, such as neat two-step or two-paragraph progression that feels preassembled

### 3.5. Prefer direct, flat, respectful statements

When a sentence can be said directly, say it directly.

Prefer:

- direct declarative sentences
- concrete subjects and concrete verbs
- calm, flat explanation instead of correction-first rhetoric
- content-telling narrative instead of commentator voice

Avoid by default:

- `不是……而是……`
- `并非……而是……`
- `不只是……而是……`
- `不靠……而是……`
- `真正`
- `真正的`
- `实际上`
- `最需要盯住的是`
- `普通人最该记住的是`
- `读这篇文章时`
- `放在一起看`
- `再往下看`

If contrast is genuinely needed to correct a likely misunderstanding, keep it once and make the correction concrete. Do not let contrast framing become the paragraph's default skeleton.

### 3.6. Remove commentator and teacher voice

High-risk signs:

- the sentence comments on how the text is written instead of what the source says
- the writer stands beside the material and tells the reader what to notice
- the writer ranks what the reader “should” remember
- the writer sounds like they are leading a class, not sharing content

Prefer:

- `图 2 里，病例组的……更高`
- `这一步只回答了……`
- `后面没有看到……`

Avoid:

- `这一点很关键`
- `最值得记住的是`
- `可以这样理解`
- `更像是在提醒我们`
- `先看……再看……`
- `这张图的作用很朴素`

### 3.7. Keep the reader relationship level

In public-facing writing, do not lower the reader's status just to sound explanatory.

Avoid:

- labeling the reader as `普通人`, `普通读者`, or similar identity-setting phrases
- management-style phrasing such as `别往后拖`, `不能轻轻放过`, `最该记住的是`
- over-helpful reader prompts that sound like seminar guidance rather than natural prose

Prefer:

- direct description of the result, risk, choice, or next step
- flat, respectful action wording
- situation-based wording such as `就医的人`, `关心这件事的人`, or no label at all

### 4. Prefer concrete Chinese rhythm

Default rhythm:

- short to medium paragraphs
- one information cluster per paragraph
- direct verbs over abstract nouns
- direct statements before summary comments
- natural spoken cadence without slang or performance
- when the draft feels too neutral or over-objective, allow a little lived voice, mild stance, or conversational texture
- let sentence length and sentence structure vary naturally; do not let a whole paragraph glide forward in the same rhythm
- allow one point to carry a sentence; do not force every list to展开得 equally full and equally balanced
- sentence length can vary; do not hard-split sentences just to create structure, and do not over-pack them just to sound deep
- optimize for natural reading rhythm: if it reads smoothly out loud, the sentence length is probably fine
- watch for “uniformly polished” rhythm: if every sentence feels equally complete and equally smooth, the paragraph probably needs one shorter, sharper, or more selective sentence
- watch for “standard review progression”: if the body keeps advancing in the same tidy two-step pattern, break the sequence with a more direct entry, a sharper sentence, or a different paragraph job

Prefer:

- `写进病历`
- `改了治疗方案`
- `漏掉了鉴别诊断`
- `整体看和指南接近`
- `讨论了 / 优化了 / 分析了`
- `我更在意的是……` when the document benefits from a visible speaker
- `说实话 / 有点可惜 / 其实` when one small oral marker helps the sentence land more naturally
- `需要尽快处理` / `建议尽快接上` when action advice is needed without sounding commanding

Avoid:

- `形成了一层变化`
- `呈现出某种底色`
- `往两边分开`
- `更吃力的部分`
- a paragraph where every sentence has nearly the same length and the same “判断 -> 解释 -> 补边界” skeleton
- lists where every item is展开得 equally smooth, equally complete, and equally weighted when the writer clearly cares more about one of them
- “concept-block” phrasing where several abstract bundles stack up in a row and the paragraph starts sounding assembled rather than written
- paragraph logic that feels pre-slotted into the same two-part review movement again and again
- sentences that exist mainly to tell the reader how to read the material
- sentences that lean on `不是……而是……` or `真正 / 实际上` to manufacture force

### 4.5. Clean up punctuation and notation habits

These edits often help when the prose feels machine-smoothed:

- in normal Chinese prose, prefer Chinese quotation marks `“ ”` over English quotes unless the source string must stay exact
- avoid using `/` as a lazy connector in body copy when `和` / `或` / `到` / `分别` / `以及` would read more naturally
- avoid using `->` to stand in for logic, sequence, or causation; write the relationship out in Chinese
- keep punctuation quiet and natural; do not rely on symbols to simulate structure

Use judgment:

- keep `/` when it is genuinely the clearest form, such as URLs, file paths, units, ratios, trial labels, or established notation
- keep exact original punctuation inside titles, code, formulas, or literal interface strings when needed
- add spaces where Chinese mixed writing benefits from them, especially around standalone English words, model names, and some number-unit combinations, but do not insert spaces mechanically into DOI, URL, gene names, or compact scientific notation
- typography cleanup should support readability, not become a separate style performance

### 5. Explain terms inside the sentence when needed

If a metric or acronym is necessary, explain it in the same sentence or paragraph.

Prefer:

- `OR 2.2，也就是在同样已经叫了救护车的人里，这组症状在后来发生心脏骤停的人身上更常见`
- `心肺复苏（CPR）`

Avoid:

- one paragraph full of metrics
- next paragraph teaching what those metrics mean

### 6. Do a final “human pass”

Before finishing, read each paragraph and ask:

- Does this sound like one person calmly explaining a real thing to another person?
- Could this sentence fit too many unrelated articles?
- Is the sentence describing the study, or describing my own summary of the study?
- Is the paragraph too smooth, too even, or too complete in a way that feels machine-optimized?
- Is the paragraph leaning on clusters of polished abstract phrases instead of concrete objects, actions, or consequences?
- Is the paragraph moving forward through a reusable template rather than through this document's own actual logic?

If the wording is generic enough to fit many unrelated drafts, rewrite it into that document's own subject, action, and result.

## Selective Human Signals

These are allowed tools, not default mannerisms.

### A. Light first-person voice can help

AI prose often over-performs neutrality with lines such as `数据显示` / `研究表明` / `结果提示` repeated again and again.

When the draft benefits from a real speaker, you may add a light first-person stance such as:

- `我更在意的是……`
- `我会这样理解……`
- `我更愿意把它看成……`

Use this when:

- the document is a commentary, newsletter, speech note, strategy memo, or public explainer that benefits from a visible speaker
- the first-person phrase clarifies emphasis, tradeoff, or judgment

Do not use first person to blur attribution. Evidence still belongs to the study, source, or document itself.

### B. Direct verbs usually sound more human

When a sentence绕一圈才落到动作，直接压平：

- `进行了讨论` -> `讨论了`
- `实现了优化` -> `优化了`
- `完成了分析` -> `分析了`

This usually makes Chinese feel less bureaucratic and less machine-smoothed.

### C. A little oral texture is okay

If the copy sounds too flat, one small口语 marker can help:

- `其实`
- `说白了`
- `对了`
- `这事儿`

Use them sparingly and only when they match the speaker and the document.

### D. Mild attitude can make the speaker feel real

A little attitude can help when the sentence otherwise sounds too polished or too careful:

- `挺重要`
- `说实话`
- `有点可惜`

Keep it light. The goal is a real person with a point of view, not a performer doing attitude.

### E. Straight talk beats expert posturing

Prefer:

- direct statements
- clear subjects and verbs
- a calm human stance

Avoid:

- sounding like a lecturer
- sounding like a detached “expert voice”
- sounding like the text is trying to manage or impress the reader

## Mode Calibration

Do not humanize every document in the same way.

### Public explainer / literature-sharing mode

Use:

- direct statements
- natural spoken rhythm
- occasional mild stance when it helps the paragraph feel spoken
- very light oral texture
- flat, respectful reader relationship

Keep restrained:

- first person should be rare
-口语词 should appear only when they truly help the sentence land
- attitude should stay mild and factual
- avoid teacher-like guidance and commentary about what the reader should focus on

### Report / PRD / README / strategy mode

Use:

- direct verbs
- simpler syntax
- fewer stock connectives
- cleaner paragraph rhythm

Usually avoid:

- first person
- oral markers
- emotional attitude words

This mode should feel human because it is clear and concrete, not because it sounds chatty.

### Personal commentary / speech / newsletter mode

You may allow:

- more visible first-person stance
- a little more oral texture
- a little more attitude

But still:

- keep facts attributed correctly
- do not let tone outrun content
- do not turn the prose into performance

## Default Rewrite Targets

- public-facing Chinese articles
- reports and memos
- PRDs and strategy drafts
- README files and documentation
- newsletter and social copy
- speech notes and presentations
- WeChat long-form prose
- literature-sharing drafts
- health and medicine explainers
- titles, leads, section headings, figure notes, takeaways

## Hard Rules

- Preserve evidence, numbers, and boundaries.
- Do not replace precision with hype.
- Do not use internet slang to fake “human warmth”.
- Do not solve AI tone by making the copy loose, cute, or exaggerated.
- Do not stop after replacing one bad phrase if the nearby prose still sounds templated.
- Prefer direct plain statements over expert-posturing. Write the fact, the number, and the boundary; do not sound like a lecturer or an authority performing expertise.
- If a sentence can be stated directly, remove the contrast phrase or emphasis word and keep the declarative statement.
- Do not default to `不是……而是……`, `并非……而是……`, `不只是……而是……`, or `不靠……而是……` as a sentence pattern.
- Do not use `真正`, `真正的`, or `实际上` as headline boosters, takeaway fillers, or emphasis crutches.
- Do not comment on the writing itself with lines such as `信息很清楚`, `边界很明确`, `最值得记住的是`, or similar meta-summary language.
- Do not write from above the reader with phrases such as `普通人最该记住的是`, `最需要盯住的是`, `别往后拖`, or similar control language when a flat statement would do.
- Treat first-person stance,口语词, and mild attitude as optional seasoning, not mandatory ingredients.
- If a sentence already sounds natural in plain Chinese, do not force extra “human signals” into it.
- Do not force colloquial metaphors onto abstract subjects. If a phrase sounds like half-oral, half-abstract Chinese such as a fabricated “spoken” collocation, rewrite it back into plain natural Chinese.

## What Helps vs. What Hurts

Some public "去 AI 腔" advice is useful, but some of it makes Chinese prose worse.

Keep these:

- vary sentence length and paragraph openings
- reduce stock connectives like `首先 / 其次 / 最后 / 综上所述`
- prefer simpler verbs over nominalized phrasing such as `进行了分析`
- mix simple and slightly longer sentences naturally
- let one stronger point interrupt a list or a paragraph when that matches human emphasis
- keep the necessary logic, but do not spell out every bridge if one concrete consequence already makes the point
- end cleanly instead of adding empty closing slogans
- clean up machine-like symbol habits such as lazy `/`, English quotes in Chinese prose, or `->` used as shorthand for logic
- when the document supports it, allow a little first-person stance instead of performing total objectivity
- use a small amount of oral texture or mild attitude when it helps the prose feel spoken by a real person
- vary repeated “objective” openers such as `研究表明 / 数据显示 / 结果提示` when the subject is already clear from context
- loosen over-standardized phrase bundles when a more human Chinese phrasing can carry the same meaning
- when a paragraph feels too symmetrical, break the rhythm with one cleaner sentence instead of polishing every sentence to the same finish
- when a judgment already lands, stop there; do not always add the extra “what this means” layer unless it is needed
- vary paragraph jobs; do not let adjacent paragraphs all move through the same “background -> explanation” review cadence
- replace contrast-first phrasing with direct statements when the sentence does not truly need a rebuttal shape
- remove rhetorical filler emphasis such as `真正` or `实际上` when the evidence already carries the point
- replace teacher-like prompts with direct content statements
- keep the reader relationship level and respectful, especially in public-facing writing

Do not do these by default:

- do not add filler particles just to sound human, such as forcing extra `的 / 了 / 到 / 过 / 会 / 有 / 能`
- do not mechanically merge short sentences into long ones
- do not deliberately reduce the number of `。` and replace them with commas or semicolons just to blur the rhythm
- do not force first-person voice such as `我觉得 / 我看来 / 我试过` into every document or every paragraph
- do not use fake intimacy or canned口语 such as `说白了 / 这事儿 / 其实很简单` as repeated mannerisms or as a substitute for substance
- do not make the prose artificially jagged just to “break AI rhythm”; rhythm variation should come from emphasis, not from randomness
- do not delete necessary reasoning steps just to avoid sounding complete; trim redundancy, not substance
- do not polish every sentence to the same density, cadence, and finish; that creates another kind of AI smoothness
- do not stack several abstract phrase bundles in one sentence when concrete Chinese can carry the point more lightly
- do not turn anti-AI polishing into forced colloquialization; a strange spoken metaphor is still bad writing
- do not let the body default to a neat two-paragraph review march if the material would read more naturally with an uneven, document-specific progression
- do not introduce errors like swapping `的 / 地 / 得` on purpose
- do not rewrite a natural factual sentence into an awkward inversion just to dodge detectors
- do not add or remove spaces mechanically just to imitate a style guide; spacing should help reading, not announce itself
- do not ban `/` or English quotes blindly when they are part of an exact title, URL, notation, or product string
- do not build momentum by negating a weaker version of the sentence first; write the stronger sentence directly
- do not turn headings, leads, figure notes, or takeaways into little lectures about what the reader should notice
- do not use `真正`, `实际上`, or similar words to simulate authority when the sentence has not yet said anything concrete

The goal is natural Chinese, not distorted Chinese.
