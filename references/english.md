# English AI-Tone Reference

Use this reference when English prose sounds too generic, too polished, too evenly structured, or too ChatGPT-like.

This reference is for restoring authorship and genre fit, not for promising detector evasion. AI detectors can misread polished human writing; do not rewrite only to satisfy a detector.

## Source-informed patterns

Recent studies and writing-center guidance point to several recurring English AI-tone signals:

- rapid growth in generic LLM-associated academic terms such as `delve`, `underscore`, `intricate`, `meticulous`, `pivotal`, `showcase`, `unveil`, `nuance`, `bolster`, `foster`, and `interplay`
- stock phrases such as `underscores the importance of`, `delve into the intricacies`, and `in today's landscape`
- predictable sentence rhythm and repeated medium-length declarative sentences
- generic or overly polished language with broad adjectives and few concrete details
- automatic transitions such as `Furthermore`, `Moreover`, `Additionally`, `Overall`, and `In conclusion`
- summary without synthesis: accurate but unowned explanation that does not show why the point matters here
- voice flattening, including the loss of local English variety, pragmatic markers, or culturally meaningful phrasing during "professionalization"

Useful source trail:

- Juzek and Ward, "Why Does ChatGPT 'Delve' So Much?" (COLING 2025), https://arxiv.org/abs/2412.11385: lexical overrepresentation in scientific English.
- Kousha and Thelwall, "How much are LLMs changing the language of academic papers after ChatGPT?" (Scientometrics, 2026), https://link.springer.com/article/10.1007/s11192-026-05601-5: multi-database and full-text analysis of LLM-associated terms.
- UNESCO, "AI and the great linguistic flattening" (2025), https://www.unesco.org/en/articles/ai-and-great-linguistic-flattening: default AI language patterns and linguistic flattening.
- Westcliff Writing Center, "Avoiding AI-Like Writing" (2025), https://writingcenter.westcliff.edu/wp-content/uploads/2025/11/Avoiding-AI-Like-Writing.pdf: predictable rhythm, generic polish, lack of synthesis, stock transitions, and flat voice.
- Navneet, Chandra, and Zhang, "When AI Writes, Whose Voice Remains?" (2026), https://arxiv.org/abs/2602.22145: cultural marker erasure in World English varieties.

## Diagnostic scan

Check whether the draft has these clusters.

### 1. Lexical fingerprints

High-risk when clustered or used vaguely:

- `delve into`, `realm`, `landscape`, `tapestry`
- `intricate`, `nuanced`, `pivotal`, `crucial`, `vital`, `robust`
- `meticulous`, `commendable`, `noteworthy`, `significant`
- `showcase`, `underscore`, `highlight`, `unveil`
- `foster`, `bolster`, `leverage`, `harness`, `empower`
- `comprehensive`, `holistic`, `seamless`, `transformative`, `innovative`

Do not ban these words mechanically. Keep them when they are the natural field term or the most precise verb.

### 2. Stock transitions and scaffolding

High-risk phrases:

- `It is important to note that`
- `It is worth noting that`
- `This highlights the importance of`
- `This underscores the need for`
- `In today's ever-evolving landscape`
- `As we navigate`
- `In this article, we will explore`
- `Let's delve into`
- `Overall`
- `In conclusion`
- `Furthermore`, `Moreover`, `Additionally`

Preferred response:

- delete the phrase if the sentence stands without it
- replace it with the actual relation: cause, limit, contrast, method, result, or implication
- use a concrete noun or verb instead of a formal bridge

### 3. Symmetrical rhetoric

High-risk skeletons:

- `not merely X but Y`
- `not just X; it is Y`
- `X is more than Y; it is Z`
- `from X to Y, A and B alike`
- `whether X or Y`
- `both X and Y`

Preferred response:

- state the main claim directly
- keep contrast only when the reader is likely to hold the wrong interpretation
- split overloaded balanced clauses into shorter, evidence-led sentences

### 4. Predictable rhythm

High-risk signs:

- most sentences are medium length
- every paragraph opens with a topic sentence, expands once, then closes with a neat mini-summary
- sentence beginnings repeat: `This`, `These`, `By`, `Through`, `In`, `As`
- every claim lands at the same emotional and argumentative weight

Preferred response:

- vary sentence length because the meaning asks for it
- let one sentence be short when it carries the point
- combine or split based on logic, not symmetry
- remove mini-conclusions that simply restate the paragraph

### 5. Generic claims without ownership

High-risk signs:

- broad claims that could fit almost any field
- no actors, dates, methods, constraints, tradeoffs, or concrete examples
- perfect fluency but no visible decision about what matters
- summary of source material without interpretation or synthesis

Preferred response:

- add specificity only from the available text or user-provided context
- name the actor, object, action, condition, result, or limitation
- make the writer's judgment visible where the genre allows it
- in academic prose, connect the point to the research question, method, finding, or evidence boundary

### 6. Voice flattening

High-risk signs:

- all personality, dialect, or local English variety has been smoothed into corporate American English
- a non-native but clear sentence is rewritten into bland "professional" English with lost pragmatic meaning
- the writer's level of certainty, hesitation, irritation, warmth, or caution disappears

Preferred response:

- preserve legitimate World English, non-native English, and domain-community phrasing when it is clear and meaningful
- improve clarity without erasing identity
- ask only if the user explicitly wants standardization for a specific audience or publication

## Rewrite patterns

Use these as tendencies, not fixed replacements.

| AI-like pattern | Better move |
| --- | --- |
| `This article will delve into X` | `This article examines X` or start with the actual claim |
| `In today's ever-evolving landscape` | Name the concrete change, market, field, date, or pressure |
| `It is important to note that X` | Delete the opener; write `X` |
| `This underscores the importance of X` | Write what the evidence shows, changes, or limits |
| `X plays a pivotal role in Y` | Write how X affects Y |
| `A comprehensive understanding of X is essential` | Write what the reader needs to know and why |
| `Leveraging X to foster Y` | `Using X to build/support/increase Y`, with a concrete object |
| `In conclusion` | Start with the final implication or decision |
| `not only X but also Y` | State X and Y directly, or keep the contrast only if needed |

## Genre lanes

### Academic English

Prioritize:

- field-specific nouns and methods
- cautious evidence verbs: `suggest`, `indicate`, `estimate`, `show`, `find`
- clear limits on scope and causality
- citation integration with signal phrases when citations are present
- concrete relation to the research question or data

Avoid:

- `This study delves into`
- inflated novelty claims
- vague praise words such as `commendable` or `groundbreaking` unless quoted or justified
- polishing away the author's actual analytic stance

#### Document-level structural AI tone in academic and framework papers

These are style and structure risk signals, not evidence that a model authored the manuscript. Judge them as clusters and by the work each passage performs; do not use a fixed count as an authorship test. Apply this scan to a whole manuscript only when the user has asked for manuscript-wide review or restructuring.

##### Cross-section semantic redundancy

High-risk signs:

- the central thesis returns in the Introduction, framework, Discussion, governance section, and Conclusion through near-synonymous wording
- a later occurrence adds no evidence, boundary condition, counterargument, operational consequence, or new inference

Preferred response:

- map each occurrence of the thesis and keep the fullest statement where it performs necessary argumentative work
- require later occurrences to add a distinct function; otherwise shorten, merge, or delete them while preserving necessary Abstract-Introduction-Conclusion correspondence

Example: `Internal consistency is not external validation` later becomes `Self-checking cannot establish clinical fitness` without a new consequence. Keep one full explanation and tie any later mention to the specific decision it changes.

##### Repeated rhetorical closure

High-risk signs:

- each section independently defines a distinction, explains it, preserves its boundary, and closes by restating it
- sections read as parallel mini-essays and repeatedly return to the same final sentence

Preferred response:

- give each section one main job, such as defining the problem, presenting evidence, testing a limit, or deriving an implication
- remove local conclusions that repeat the manuscript thesis rather than completing that section's distinct task

Example: three consecutive sections all end with `X may support Y, but it cannot establish Z.` Let the first define the boundary; use the later sections for evidence and consequences instead of another closure.

##### Over-neat taxonomy

High-risk signs:

- the manuscript repeatedly converts material into limits, risks, gates, tiers, states, classes, levels, matrices, or other named sets
- the number and neatness of categories exceed what the conceptual contribution or decision problem requires

Preferred response:

- retain a taxonomy when its categories change interpretation, evaluation, decision, or action
- merge decorative categories and preserve a defensible human-designed framework when each component has independent analytical work

Example: `five limits -> five risks -> two gates -> four states -> four action classes` may be one useful framework or several restatements. Test what decision changes at each step before keeping all five layers.

##### Conceptual relabeling

High-risk signs:

- the same distinction is successively renamed as a boundary, gate, state, tier, model, or framework
- a new label introduces no new variable, relationship, testable proposition, or operational meaning

Preferred response:

- inventory defined terms and group labels that point to the same underlying distinction
- keep the smallest stable vocabulary that preserves genuine conceptual differences

Example: `verification boundary`, `validation gate`, and `use-state boundary` should not all survive merely because they sound progressively formal. Keep separate labels only if each controls a different inference or action.

##### Low analytical increment

High-risk signs:

- a fluent abstract paragraph sounds correct but supplies no new evidence, constraint, scope condition, counterexample, or executable consequence
- paraphrase and rhetorical emphasis create the appearance of progression

Preferred response:

- ask what the passage changes in the argument; merge or delete it if the answer is nothing
- add specificity only from the manuscript or user-provided sources, never by inventing examples, evidence, or objections

Example: `This distinction is crucial and further underscores the importance of preserving the boundary` adds emphasis, not analysis. Replace it with the supported consequence, or delete it.

##### Contribution-to-length imbalance

High-risk signs:

- manuscript length grows faster than its evidential or conceptual contribution
- one compact claim receives separate definitions, taxonomies, frameworks, transitions, and recaps without corresponding analytical gain

Preferred response:

- use the deletion test: if removing a passage loses no evidence, reasoning step, boundary, or conclusion, compress or remove it
- do not pursue brevity mechanically; retain necessary methods, results, definitions, limitations, and field-required explanation

Example: a one-sentence distinction does not need a definition section, a two-gate restatement, an evidence-state restatement, and a full concluding recap unless each adds a different function.

##### Unchallenged central thesis

High-risk signs:

- the manuscript repeatedly confirms its main claim but never examines scope limits, failure conditions, competing explanations, or a nearby existing framework
- apparent critical depth comes from restating the thesis more forcefully rather than testing it

Preferred response:

- recover supported qualifications, exceptions, and competing interpretations already present in the manuscript or supplied sources
- treat this as an academic-argument quality check, not an authorship test, and do not invent a counterargument merely to make the prose look human

Example: after establishing `X cannot establish Y`, a later section should clarify where X remains useful, when the boundary may be uncertain, or what evidence would change the conclusion if the available sources support those points.

#### Scientific and medical table language

For biomedical, translational, oncology, or molecular-biology manuscripts, table text can sound AI-generated even when the grammar is correct. The main risk is not stock adjectives; it is an internal framework label that does not match the field's usual table language.

Before rewriting a biomedical table, ask:

- Is this a column heading, a category label, an evidence level, or a concrete assay/readout?
- Is the term already defined in the manuscript, and is it a standard term in the field?
- Would the replacement change the evidence strength or clinical claim?
- Will the replacement make the table too long or disturb protected values, units, or statistics?

High-risk signs:

- column heads such as `Framework role`, `Evidence anchor`, `Decisive test`, or `Why it matters`
- self-made category labels such as `low-X suppressive module`, `adaptive protein-state module`, `core immune-microenvironmental module`, or `boundary-setting only`
- vague umbrella terms such as `evidence`, `interpretive boundary`, `signal`, `criteria`, `context`, `readout`, `claim`, or `framework` when the table or caption does not specify the biological layer, assay type, clinical setting, or validation endpoint
- compressed clinical phrases such as `clinical direction`, `validation-stage`, `restoration selection`, `immune-safety checks`, or `spatial/cell phenotyping`
- slash-heavy assay wording such as `IHC/MS`, `RNA/protein`, `methylation/expression`, or `prognosis/restoration` when the relation should be explicit
- gene/protein mixing, for example using a gene symbol where the readout is a protein, aggregate, conformation, or subcellular localization

Preferred moves:

- replace internal labels with evidence-table language: `Proposed interpretation`, `Evidence base`, `Supporting evidence`, `Key caveat`, `Validation focus`, `Key validation test`, `Rationale`
- use biomarker language only at the evidence level the study supports: `clinical validation`, `clinical utility`, `predictive utility`, `prognostic evidence`, `candidate biomarker`, `treatment-by-biomarker interaction`
- for early association or mechanistic work, prefer `clinical relevance`, `potential clinical implication`, or `translational relevance` over `clinical utility` or `clinical actionability`
- replace `module` with `pattern`, `phenotype`, `evidence pattern`, or `context` unless the text truly describes a standard module, such as a WGCNA module, gene module, pathway module, network module, co-expression module, immune-cell module, spatial module, or module score
- name the restoration target: `target-gene re-expression`, `target rescue`, `forced expression of the target gene/protein`, or `pathway activation/reactivation`
- separate levels of measurement: gene symbols for DNA-level alteration, methylation, and gene/RNA expression; protein names, approved protein symbols, or marker names for protein expression, abundance, aggregation, conformation, proteoforms, PTMs, or localization
- reduce slash compression with `and`, `with`, `or`, semicolons, or short noun phrases when the relation is unclear; keep compact slash forms when the table is space-constrained and the meaning is already defined
- replace vague umbrella terms with the specific biological or clinical meaning in that context: assay support, functional perturbation data, clinical association, cellular source, tumor lineage, treatment setting, measured biological layer, protein-state measurement, immune-cell abundance, validation endpoint, or unresolved biological inference
- in figure captions, name what is being measured or validated before naming the interpretation; for example, write `SNCA RNA expression and promoter methylation across tumor lineages` before `lineage-specific signal`
- in table headers, prefer a short precise label plus a clarifying footnote over a broad label that only makes sense inside the author's private framework

Semantic specificity checks:

- `evidence` should say what kind of evidence: `assay support`, `functional support`, `clinical association`, `cohort-level association`, `single-cell support`, `spatial pathology support`, `perturbation data`, or `protein-state validation`
- `signal` or `readout` should say what is measured: `RNA expression`, `promoter methylation`, `protein abundance`, `aggregate burden`, `subcellular localization`, `immune-cell abundance`, or `treatment-response association`
- `interpretive boundary` should say what remains unresolved: `unresolved cellular source`, `unresolved protein state`, `unresolved causality`, `unresolved treatment interaction`, or `biological inference not yet established`
- `criteria` should say what decision it supports: `validation endpoint`, `translational prerequisite`, `assay-performance requirement`, `clinical-utility requirement`, or `safety requirement`
- `context` should say which context: `tumor lineage`, `cellular source`, `protein state`, `treatment setting`, `disease stage`, or `sample type`

Useful replacements:

| Risky table wording | More field-typical option |
| --- | --- |
| `Framework role` | `Proposed interpretation` / `Biological interpretation` |
| `Evidence anchor` | `Evidence base` / `Supporting evidence` |
| `Evidence` | `Functional support`, `Assay support`, `Clinical association`, `Validation data`, or `Study-level data`, depending on the source |
| `Supporting evidence` | `Key assay or functional support` when the evidence is experimental; `Clinical association` when it comes from patient cohorts |
| `Interpretive boundary` | `Unresolved biology` / `Unresolved cellular source` / `Unresolved protein state` / `Biological inference not yet established` |
| `Signal` / `Readout` | `Measured biological layer` / `Molecular measurement` / `Protein-state measurement` / `Immune-cell abundance` |
| `Criteria` | `Validation endpoint` / `Translational prerequisite` / `Assay-performance requirement` |
| `Context` | `Tumor lineage` / `Cellular source` / `Treatment setting` / `Sample type` |
| `Claim` | `Biological inference` / `Biomarker use` / `Therapeutic rationale` / `Clinical conclusion` |
| `Decisive test` | `Key validation test` / `Critical validation test` |
| `Why it matters` | `Rationale` / `Translational rationale` |
| `clinical direction` | `clinical relevance` / `clinical guidance`; use `clinical actionability` only when supported by decision-level evidence |
| `predictive use` | `predictive utility` when comparator or treatment-interaction evidence exists; otherwise `predictive relevance` / `candidate predictive marker` |
| `validation-stage` | as a heading: `Validation status` / `Stage of validation`; as a cell: `Candidate biomarker; clinical validation pending` / `Requires validation` |
| `localization-shifted protein` | `altered subcellular localization of the protein` |
| `immune-safety checks` | `immune safety assessments` |
| `restoration selection` | `restoration-relevant biology` / `candidate restoration contexts` |

Do not replace these mechanically. If a term is explicitly defined in the manuscript and is defensible for the field, keep it; otherwise prefer the wording a reviewer would expect in an evidence table, figure legend, or biomarker-validation summary. Preserve the evidence strength: do not upgrade an association into mechanism, clinical utility, or therapeutic actionability. Preserve table structure, units, statistics, P values, confidence intervals, HR/OR/RR labels, gene-symbol capitalization, protein names, and italic/non-italic conventions unless the user explicitly asks to fix them.

### Business, product, and technical writing

Prioritize:

- owner, action, object, deadline, constraint, and measurable result
- plain verbs: `use`, `build`, `ship`, `test`, `reduce`, `increase`, `remove`, `compare`
- exact product names, API names, commands, UI labels, and paths

Avoid:

- `seamless`, `robust`, `leverage`, `empower`, `transformative`, `cutting-edge`
- strategy fog: `drive impact`, `unlock potential`, `enhance efficiency` without a metric or action
- paragraph conclusions that say the work is important instead of naming the next step

### Public articles and newsletters

Prioritize:

- a direct lead
- concrete people, events, numbers, or tensions
- a visible point of view without over-explaining
- rhythm that fits the outlet and audience

Avoid:

- tour-guide phrasing such as `Let's explore`
- moral-of-the-story endings
- over-neat three-part framing when the topic is messier

### Emails and workplace messages

Prioritize:

- the ask
- the reason
- the deadline or next step
- the relationship tone

Avoid:

- over-polite padding
- generic gratitude chains
- `I hope this email finds you well` unless it fits the relationship
- long context paragraphs before the actual request

## Final English self-check

Ask:

- Are any high-risk words clustered without doing precise work?
- Can the reader point to a concrete actor, object, action, condition, or consequence?
- Did I remove transitions that only decorate the logic?
- Does the paragraph still have the same sentence rhythm from start to finish?
- Does the writer's judgment show up where the genre allows it?
- Did I preserve the writer's English variety, professional register, and evidence boundary?
