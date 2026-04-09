---
name: de-ai-chinese-writing
description: Rewrite Chinese prose so it reads more naturally and less like AI-generated text while preserving facts, evidence, logic, and domain meaning. Use when the user asks to 去 AI 腔, make writing more human, more自然, more口语化但不油滑, less像教科书, less像模板, or when any Chinese draft feels over-structured, repetitive, connector-heavy, vague, lexically flat, voice-less, or machine-smoothed. Works across articles, reports, theses, academic prose, PRDs, product copy, README files, presentations, newsletters, and other Chinese writing tasks.
---

# De-AI Chinese Writing

Use this skill to turn stiff, templated, or machine-smoothed Chinese into natural human prose without flattening the substance or faking personality.

Read `references/markers.md` when you need concrete examples of AI-like phrasing patterns and preferred rewrites.
Read `references/rewrite_patterns.md` when you want phrase-level before/after rewrite patterns you can apply quickly.
Read `references/risk_words_quicklist.md` when you want a fast sweep for high-risk words and their more natural Chinese alternatives.
Read `references/thesis-medical.md` when the task is a thesis, dissertation, medical paper, academic discussion section, or other formal Chinese scholarly prose where genre-appropriate wording matters as much as sentence smoothness.

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
- break over-smoothed rhythm when sentence length, sentence structure, or paragraph movement feels too even
- trim over-explained logic when the paragraph insists on spelling out every bridge instead of carrying one decisive point
- cut low-information connective openers
- remove commentary about the writing itself
- collapse textbook-style explanation scaffolding into direct content statements
- vary repeated sentence templates and paragraph openings
- clean up punctuation habits that make Chinese look machine-smoothed

Bad pattern:

- `这篇研究最值得记住的是……`
- `这更像是在提醒我们……`
- `结果落到……`
- `大面上……`

Preferred pattern:

- say what happened
- say what changed
- say what the number means
- say where the evidence stops

Recommended pass order:

1. remove commentary about the writing itself
2. replace slippery words and translationese abstract nouns
3. simplify nominalized phrasing and over-standardized phrase bundles
4. break over-even rhythm and trim over-complete explanation
5. reduce repeated connectives and repeated “objective” openers
6. add a little human texture only if the paragraph still feels too flat

Pay special attention to these common AI-polish symptoms:

- the sentences are too even in length, structure, and landing point
- every judgment is wrapped up too fully, leaving no natural white space
- abstract phrase bundles appear in clusters and start to feel like concept blocks rather than lived Chinese
- the paragraph logic falls into a standard review-style push every time, such as neat two-step or two-paragraph progression that feels preassembled

### 3.5. Check whether the wording fits the discourse community

Some words are grammatically smooth but still sound wrong for the document type.

This matters especially in:

- theses
- medical papers
- technical reports
- formal Chinese academic prose

High-risk mismatch:

- product or consulting language inside an academic paragraph
- engineering workflow nouns inside a medical interpretation paragraph
- “polished” abstract nouns that are not how people in that field usually write

Examples:

- `证据链` -> depending on context, often better as `验证框架` / `结果框架` / `证据体系`
- `闭环` -> often better as `前后对应` / `相互印证` / `形成完整验证`
- `交付物` -> often better as `材料` / `输出材料` / `补充材料`
- `核对` -> in formal medical prose often better as `复核` / `比较` / `一致性检查`
- `线索` -> when not truly exploratory, often better as `依据` / `特征` / `候选因素` / `结果`
- `提醒` -> often better as `提示` / `表明` / `说明`

Do not replace these mechanically. Decide from the sentence's role:

- exploratory finding
- formal conclusion
- method description
- heading
- caption

When working on a thesis or medical paper:

- prefer field-typical nouns over polished but generic abstractions
- distinguish exploratory wording from confirmatory wording
- treat headings, captions, methods, results, and discussion as different subgenres
- keep figure titles, automatic fields, and citation-heavy sentences conservative unless the task explicitly allows broader rewriting
- when the prose starts “managing the argument” with words like `框架` / `体系` / `路径` / `主线` / `支撑` / `结果整合`, check whether the sentence is describing the writing rather than the study
- if a sentence can be rewritten by naming the object, action, comparison, or evidence directly, prefer that over abstract organizing nouns

### 3.6. Check for transition-word overload and repeated sentence skeletons

AI-flavored Chinese often does not fail at vocabulary first. It often fails at paragraph motion.

High-risk signs:

- too many connective openers such as `从方法学上看` / `从科学问题看` / `综上` / `据此` / `为此` / `换句话说`
- too many academic transition words such as `此外` / `然而` / `总之` / `同时` / `值得注意的是` used to push the paragraph forward
- the paragraph depends on transition markers to create motion instead of letting facts, objects, actions, or results carry the logic
- several nearby paragraphs starting with the same discourse move
- repeated balanced structures like `第一…第二…第三…` or `其一…其二…`
- repeated sentence skeletons like `在X任务中，…` / `本文……并……` / `若……则……`
- a paragraph that is grammatically perfect but feels over-packed, over-even, and overly well-managed
- a paragraph where every sentence is syntactically complete in the same way, lands at the same weight, and shows no natural variation in pressure or release

Preferred response:

- remove the connective if the sentence still stands without it
- if the relation is obvious from context, delete the transition word instead of keeping a formal bridge
- if the relation needs to stay, write the relation out through object, action, comparison, sequence, or consequence instead of leaning on stock markers
- vary paragraph openings across adjacent paragraphs
- collapse repeated skeletons into more direct statements
- turn “writing-management” sentences into object-action-result sentences
- keep the grammar correct, but break machine-like uniformity by varying sentence length, clause count, and where the sentence lands
- let one sentence stop earlier when the judgment already lands; do not always complete the same “judgment -> explanation -> boundary” package
- in thesis writing, inspect clusters rather than isolated sentences

Interpretation note:

- `less perfect` does not mean adding mistakes
- “grammar consistency” becomes a risk when every sentence is equally polished, equally complete, and equally well-behaved
- for formal Chinese prose, “too perfect” usually means every sentence is over-packed, over-formal, and equally polished
- fix this by restoring natural variation in sentence length, weight, and directness, not by introducing grammatical errors or colloquial slackness

Highest-risk zones:

- Chinese abstract
- literature review and research-gap paragraphs in the introduction
- summary paragraphs at the end of results sections
- discussion and conclusion

### 3.7. Check for lexical flatness, not just wrong words

AI-like Chinese often does not sound bad word-by-word. It sounds as if every sentence picked the safest possible word.

High-risk signs:

- the same abstract nouns repeating across nearby paragraphs, such as `结果` / `问题` / `框架` / `分析` / `结论`
- the same soft interpretation verbs repeating, such as `提示` / `表明` / `说明`
- adjacent sentences all using the same polished adjectives, such as `稳定` / `一致` / `显著`
- paragraph after paragraph staying at the same lexical altitude: competent, generic, and hard to distinguish from other drafts

Preferred response:

- vary wording by paragraph role: observation, comparison, interpretation, limitation, implication
- prefer field-typical concrete nouns over safe but generic abstractions
- use more specific verbs when the evidence allows, such as `高于` / `低于` / `集中在` / `纳入` / `比较` / `复核`
- do not chase novelty for its own sake; avoid thesaurus-style synonym churn
- when one precise word carries the paragraph best, keep it; lexical diversity should come from function, not decoration

### 3.8. Add authorial stance when the genre allows it

Human writing often has not only content, but selective emphasis. In formal Chinese prose, this does not mean anecdotes.

For theses, medical papers, and academic prose:

- do not invent memoir-like details, anecdotes, or personal stories
- do allow a calm authorial stance: what this study focuses on, what it does not claim, what matters most, where the boundary lies

Useful patterns:

- `本文更关心的是……`
- `本研究不打算回答……`
- `这里更直接的问题是……`
- `对本研究而言，关键在于……`
- `最强证据来自……`

Avoid:

- generic impersonal prose that could fit any unrelated paper
- fake warmth
- diary-like first-person narration
- strong personal performance where the genre requires restraint

### 3.9. For doctoral theses, prefer real research trace over generic completeness

Human doctoral writing usually does not win by sounding more ornate. It wins by leaving signs that the author actually did the work.

High-risk signs:

- the research question appears fully formed, with no sense of where it came from
- the literature review treats almost every cited paper as equally important
- the methods read like a clean design spec with no tradeoff, instability, or local constraint
- the results section presents everything at the same volume
- the discussion expands upward but does not mark what the work cannot yet show
- the whole document sounds evenly polished but weakly tied to any disciplinary stance

Preferred response:

- let the question grow from prior work, data structure, method gap, or practical constraint
- let the review show selectivity, not equal-weight summary
- preserve real research friction when the source supports it: unstable training, encoding bias, sample sparsity, quality-control limits, interpretability tradeoffs
- distinguish main results, supporting results, and results that are notable but still limited
- state contribution together with limit and reach
- preserve the writer's disciplinary texture instead of averaging everything into neutral academic prose

Do not simulate “humanity” by inventing failed experiments, fake struggle, anecdotes, or deliberate roughness.

### 4. Prefer concrete Chinese rhythm

Default rhythm:

- short to medium paragraphs
- one information cluster per paragraph
- direct verbs over abstract nouns
- natural spoken cadence without slang or performance
- let sentence length and sentence structure vary naturally; do not let a whole paragraph glide forward in the same rhythm
- when one point clearly matters more, let that point carry the sentence instead of polishing every item to equal weight
- if the draft feels too neutral or over-objective, allow a little lived voice or mild stance when the genre supports it
- syntax can stay correct throughout, but it should not feel as if every sentence was finished by the same polishing template

Prefer:

- `写进病历`
- `改了治疗方案`
- `漏掉了鉴别诊断`
- `整体看和指南接近`
- `讨论了`
- `优化了`
- `分析了`

Avoid:

- `形成了一层变化`
- `呈现出某种底色`
- `往两边分开`
- `更吃力的部分`
- a paragraph where every sentence has nearly the same length and the same “judgment -> explanation -> boundary” skeleton
- lists where every item is equally smooth, equally complete, and equally weighted when the writer clearly cares more about one of them

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
- Is the paragraph too smooth because every sentence plays a neat structural role?
- Are nearby paragraphs opening in the same way or using the same skeleton?
- Are nearby paragraphs relying on the same few safe nouns or verbs?
- Does the paragraph have a calm authorial stance, or does it sound like no one is actually making choices?
- Does this sound like someone who actually worked on the problem, or someone summarizing how such work is usually described?
- Can I see the problem boundary, research friction, and result hierarchy?

If the wording is generic enough to fit many unrelated drafts, rewrite it into that document's own subject, action, and result.

## Mode Calibration

Do not humanize every document in the same way.

### Public explainer / literature-sharing mode

Use:

- direct statements
- natural spoken rhythm
- occasional mild stance when it helps the paragraph feel spoken
- very light oral texture

Keep restrained:

- first person should be rare
- oral markers should appear only when they truly help the sentence land
- attitude should stay mild and factual

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

### Thesis / medical / academic mode

Use:

- field-typical nouns
- conservative sentence handling in methods, captions, and citation-heavy passages
- calm authorial stance when emphasis or boundary-setting helps
- wording that distinguishes observation, interpretation, and limitation

Keep restrained:

- oral markers
- conversational attitude
- product, consulting, or engineering workflow language that does not belong to the field

## Default Rewrite Targets

- public-facing Chinese articles
- reports and memos
- theses and academic prose
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
- Do not let transition words carry logic that the sentence itself should carry.
- Do not keep a smooth but genre-misaligned word just because it sounds polished; prefer wording that people in that field actually use.
- Do not fake personal voice with anecdotes or memoir-like insertions in formal prose.
- Do not force lexical diversity by swapping in flashy synonyms that weaken precision.
- Do not fabricate research friction, discarded options, or limitations that are not supported by the source text.
- Prefer direct plain statements over expert-posturing.
- Treat first-person stance, oral markers, and mild attitude as optional seasoning, not mandatory ingredients.
- If a sentence already sounds natural in plain Chinese, do not force extra “human signals” into it.
- Do not confuse “human variation” with adding errors; the goal is natural variation, not broken grammar.
- Do not force colloquial metaphors onto abstract subjects. If a phrase sounds half-oral and half-abstract, rewrite it back into plain natural Chinese.
