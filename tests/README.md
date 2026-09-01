# Validation and behavior tests

Run the repository contract tests with Python's standard library:

```bash
python -m unittest discover -s tests -v
```

The automated tests verify portable frontmatter, reference paths, core safety boundaries, required document-level audit concepts, worked-example coverage, local README links, and the absence of machine-specific paths.

`behavior_cases.json` contains read-only decision tests. They intentionally assert decisions and invariants rather than exact generated wording:

- a long Viewpoint with one thesis relabeled across multiple sections should trigger a document-level recurrence map and compression plan;
- a taxonomy whose categories change evidence, actions, and claim boundaries should be retained;
- a paragraph-only request should not authorize full-manuscript restructuring.

These cases do not call an AI detector, modify user documents, or claim deterministic model output. They are suitable for manual forward-testing with any Agent Skills-compatible client.
