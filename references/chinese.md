# 中文去 AI 腔参考

Use this reference when the draft is Chinese, or when a mixed-language draft has Chinese as the main prose.

## Load more detail when needed

- Read `references/markers.md` for concrete examples of AI-like Chinese phrasing and preferred rewrites.
- Read `references/rewrite_patterns.md` for phrase-level before/after patterns.
- Read `references/risk_words_quicklist.md` for a fast sweep of high-risk words and natural alternatives.
- Read `references/thesis-medical.md` for theses, dissertations, medical papers, formal academic prose, and discussion sections.
- Read `references/execution-patterns.md` for long documents, layout-sensitive files, or staged rewriting.

## Core Chinese priorities

Keep facts fixed first:

- factual claim
- source type or document role
- sample size or key numbers
- effect direction
- limitation, scope, or evidence boundary

Then remove the machine-smoothed surface:

- replace vague slippery words with concrete subjects, actions, and outcomes
- replace translationese abstract nouns with natural Chinese when a direct expression exists
- cut low-information connective openers
- remove rhetorical booster words such as `真正`, `实际上`, and `最值得` when they only prop up tone
- remove commentary about the writing itself
- remove teacher-like prompts such as `可以这样理解`, `先看`, `再看`, and `读这篇文章时`
- reduce contrast-first framing such as `不是……而是……`, `并非……而是……`, and `不只是……而是……` when the contrast is not essential
- break over-even rhythm and repeated paragraph openings
- clean up punctuation habits that make the prose look machine-smoothed

## Prefer direct, flat, respectful statements

Prefer:

- direct declarative sentences
- concrete subjects and concrete verbs
- content-telling narrative instead of commentator voice
- calm explanation instead of correction-first rhetoric
- flat, respectful reader relationship

Avoid by default:

- `这一点很关键`
- `最值得记住的是`
- `可以这样理解`
- `更像是在提醒我们`
- `普通人最该记住的是`
- `放在一起看`
- `再往下看`

If contrast is genuinely needed to correct a likely misunderstanding, keep it once and make the correction concrete. Do not let contrast framing become the paragraph's default skeleton.

## Clean up punctuation habits

These edits often help when Chinese prose feels machine-smoothed:

- prefer Chinese quotation marks `“ ”` over English quotes unless the source string must stay exact
- avoid using `/` as a lazy connector in body copy when `和` / `或` / `到` / `分别` / `以及` would read more naturally
- avoid using `->` to stand in for logic, sequence, or causation; write the relationship out in Chinese
- avoid overusing the em dash `——` as an all-purpose connector. AI-flavored Chinese tends to stack `——` everywhere it needs to explain, qualify, elaborate, or summarize, which makes the prose feel over-managed and uniformly paced. Keep `——` for cases where a real aside, correction, or deliberate pause is needed; for most other uses switch back to plain punctuation or rewrite into a clean sentence.
- keep punctuation quiet and natural; do not rely on symbols to simulate structure

High-risk em-dash patterns and preferred rewrites:

- `A——B` used to rename or define → use `，即 B` / `，也就是 B` / `：B` / make it a new sentence, or remove the mark entirely when B is a short apposition that reads fine with a comma
- `A——因为 B` / `A——它 B` used to extend an explanation → split into two sentences; let the period do the work
- `A——B——C` stacking multiple dashes in one sentence → rewrite into two or three shorter sentences, or convert inner segments to relative clauses
- `A 是……——它做了 X、Y、Z` used to append a list → end the first clause with `。`, then start a new sentence (`它做了 X、Y、Z。`)
- `句尾 ——最后/结果/也就是……` used for punchline → delete the dash and let the prior sentence land; start a fresh sentence if the follow-up is substantive
- repeated `——` across adjacent paragraphs even when each single use is fine → vary paragraph openings and closings so the mark does not become the paragraph's rhythm signature

Diagnostic threshold:

- if a fragment longer than ~300 Chinese characters contains more than about 4 `——` marks, treat this as overuse and do a sweep
- if two consecutive sentences both use `——`, rewrite at least one of them with plain punctuation
- em dash overuse usually travels with other AI-tone patterns (contrast framing, booster words, commentator voice). Fixing the dash often opens space to fix those too.

Use judgment:

- keep `/` when it is genuinely the clearest form, such as URLs, file paths, units, ratios, trial labels, or established notation
- keep `——` when the aside is genuinely parenthetical, the pause is deliberate, or the source text itself uses it; the rule is against reflexive stacking, not against ever using the mark
- keep exact original punctuation inside titles, code, formulas, or literal interface strings when needed
- typography cleanup should support readability, not become a separate style performance

## Watch paragraph motion

Chinese AI flavor often comes from paragraph motion, not only vocabulary.

High-risk signs:

- too many connective openers such as `从方法学上看`, `从科学问题看`, `综上`, `据此`, `为此`, and `换句话说`
- too many academic transition words such as `此外`, `然而`, `总之`, `同时`, and `值得注意的是`
- several nearby paragraphs starting with the same discourse move
- repeated structures like `第一…第二…第三…` or `其一…其二…`
- repeated skeletons like `在 X 任务中，…`, `本文……并……`, or `若……则……`
- grammatically perfect paragraphs that feel over-packed, over-even, and overly managed

Preferred response:

- delete the connective if the sentence still stands without it
- if the relation is obvious from context, let context carry it
- if the relation must stay, express it through object, action, comparison, sequence, or consequence instead of stock markers

## Check titles, captions, and editorial read-feel

Chinese public articles and explainers can still feel AI-written after the body is polished if the title, section headings, captions, or summary boxes keep an editorial commentary voice.

Title risks:

- vague endings such as `给出线索`, `结果与边界`, `值得关注`, `带来启示`, and `说明了什么`
- titles that only name an abstract mechanism, module, pathway, or framework without a reader-facing question, group, result, or consequence
- titles that sound like a paper archive entry rather than a reason to read

Prefer titles that make the meaning clear quickly:

- the concrete question being answered
- the people, condition, product, or decision involved
- the result, tradeoff, risk, or downstream consequence

Editorial read-feel risks:

- `核心信息是`
- `主线很清楚`
- `证据边界也要放在前面`
- `读完后的现实落点`
- `这篇论文能支持什么`
- `这篇研究给出的启示是`

These phrases are often factually harmless, but they put the writer beside the material, commenting on the article's value. Rewrite them into the underlying fact, result, decision, or limitation.

Caption and figure-note risks:

- `图 X 给出关键对照`
- `图 X 交代数据规模`
- `图 X 串起整个过程`
- `图 X 锚定了结论`

Prefer direct image reading:

- `图 X 中，A 和 B 差异不明显；C 在病例组更高。`
- `图 X 列出样本和数据规模：...`
- `图 X 把早期反应和晚期反应分开。`

For headings and summary boxes, ask whether the line can be understood without reading the writer's intent. If the line mainly says "this paragraph is important," replace it with what is important.

## Mode calibration

Public explainer or literature-sharing mode:

- be direct and readable
- avoid lecturer voice
- keep reader labels respectful or omit them
- use mild human texture only if the genre allows it

Report, PRD, README, or strategy mode:

- name the object, action, result, and owner
- avoid inflated nouns such as `赋能`, `闭环`, `抓手`, and `体系化` unless they are precise local terms
- keep technical names, commands, paths, and UI labels exact

Thesis, medical, or academic mode:

- preserve evidence-reporting verbs and field-typical terms
- do not add first person, oral markers, attitude words, or casual texture
- distinguish headings, captions, methods, results, discussion, and limitations as separate subgenres
- avoid turning study statements into colloquial observations
- prefer real research trace over generic completeness

## Final Chinese self-check

Ask:

- Did I preserve the claim and evidence boundary?
- Did I remove writing-about-writing?
- Did I replace vague abstractions with concrete objects or actions?
- Did I reduce repeated connectives and sentence skeletons?
- Does the result sound like a person writing this genre, not a model managing a paragraph?
