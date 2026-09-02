# Behavior evaluation specification

[`cases.json`](cases.json) contains twelve synthetic fixtures for forward-testing `de-ai-writing`. The fixtures describe what a rewrite must preserve and which decisions the skill should make; they do not contain model outputs or claim that a model has passed.

Each case records:

- the language and genre;
- a self-contained synthetic input;
- protected claims that must survive any revision;
- expected editing decisions;
- forbidden outcomes;
- the expected result shape.

The deterministic repository tests validate this structure and its coverage. They do not judge prose quality, call a model, use an AI detector, or modify a user document.

## Manual forward test

1. Select one fixture and give its `input` to an Agent Skills-compatible client with `de-ai-writing` enabled.
2. Ask for the task implied by the case's genre and expected result shape. Do not provide the expected decisions as a suggested answer.
3. Compare the result with `protected_claims`, `expected_decisions`, and `forbidden_outcomes`.
4. Record the client, model, date, skill commit, and observed failures separately from this specification.

Use only synthetic or publishable material. Do not add unpublished manuscripts, patient information, confidential peer review, credentials, or detector scores to the fixtures.
