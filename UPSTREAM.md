# Provenance and design notes

This repository began as a focused Chinese-language editing skill and grew into a bilingual Agent Skill. The current version keeps the original meaning-preservation goal while adding distinct Chinese and English lanes, cautious academic and medical editing, World English preservation, and document-level structural review.

## Capabilities added during development

- general `de-ai-writing` entry point for both Chinese and English
- language-lane routing through `references/chinese.md` and `references/english.md`
- stronger academic / thesis / medical guidance
- explicit checks for transition-word overload such as `此外` / `然而` / `总之`
- explicit checks for overly uniform grammar and sentence landing
- English AI-tone guidance for lexical overrepresentation, stock transitions, predictable rhythm, generic claims, and voice flattening
- extra quick references for phrase-level rewrites and risk words
- Chinese thesis and medical guidance in `references/thesis-medical.md`
- long-document execution guidance in `references/execution-patterns.md`

## External reference consulted

- reference repo: `https://github.com/chi111i/BypassAIGC`

What was borrowed in spirit:

- segmented processing for long documents
- skipping very short or structural segments by default
- staged processing when the document is large or layout-sensitive
- compact history or style-memory summaries instead of carrying full context
- strict output contracts and terminology protection

What was deliberately not borrowed:

- verbosity expansion as an anti-AI tactic
- systematic addition of helper words such as `的` / `地` / `所` / `会`
- forcing longer sentences to simulate “humanity”
- prompt patterns that make Chinese more full, more explanatory, and more uniformly polished

No text or rules were copied verbatim. The useful idea was the workflow boundary: segment long documents, protect structure, and keep compact style memory. The choices rejected above remain rejected because they trade accuracy and author voice for detector-oriented surface changes.
