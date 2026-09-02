# Validation and behavior tests

Run the repository contract tests with Python's standard library:

```bash
python -m unittest discover -s tests -v
```

The automated tests verify portable frontmatter, reference paths, core safety boundaries, required document-level audit concepts, worked-example coverage, local README links, and the absence of machine-specific paths.

The suite also validates the Claude Code plugin metadata and the structure and coverage of [`evals/cases.json`](../evals/cases.json). These checks confirm that the fixtures are complete and internally consistent; they do not execute a model or score prose quality.

`behavior_cases.json` contains read-only decision tests. They intentionally assert decisions and invariants rather than exact generated wording:

- a long Viewpoint with one thesis relabeled across multiple sections should trigger a document-level recurrence map and compression plan;
- a taxonomy whose categories change evidence, actions, and claim boundaries should be retained;
- a paragraph-only request should not authorize full-manuscript restructuring.

These cases do not call an AI detector, modify user documents, or claim deterministic model output. They are suitable for manual forward-testing with any Agent Skills-compatible client.

The twelve cases under [`evals/`](../evals/README.md) extend this specification to English academic evidence, Chinese medical statistics, workplace email scope, long-document recurrence, functional taxonomies, World English, ranking, simultaneity, sourced objections, protected titles and proper names, and local-edit authorization.

`plugin_submission_cases.json` contains the five positive and three negative reviewer cases required for the OpenAI Plugin Directory submission. Every prompt is synthetic and self-contained, requires no authentication or private fixture, and specifies expected behavior and result shape rather than exact wording.
