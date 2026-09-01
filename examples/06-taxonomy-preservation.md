# Taxonomy preservation: a negative control

**Case type:** English academic framework
**Source status:** Synthetic demonstration
**Goal:** Show that a neat taxonomy is not automatically an AI-tone problem.

## Input

> We distinguish three evidence states for deployment decisions. In the technical state, the system has passed reproducibility and failure-recovery tests but has not been evaluated with patient data; it may proceed to controlled data-pipeline testing, but no clinical claim is permitted. In the retrospective clinical state, performance has been evaluated on a held-out historical cohort; the system may proceed to a prospective silent study, but clinicians must not receive its output. In the prospective clinical state, performance and workflow effects have been evaluated prospectively in the intended setting; deployment may be considered subject to the study's limitations and local governance. These states separate technical readiness, retrospective clinical performance, and prospective workflow evidence.

## Functional test

| State | Evidence added | Decision changed | Claim boundary |
| --- | --- | --- | --- |
| Technical | reproducibility and recovery tests | controlled pipeline testing | no clinical claim |
| Retrospective clinical | held-out historical cohort | prospective silent study | no clinician-facing output |
| Prospective clinical | prospective intended-setting evidence | deployment may be considered | only within study and governance limits |

Each category changes both the next action and the permissible claim. The taxonomy therefore performs analytical work.

## Preferred response

Retain all three states. Tighten only the final sentence, which repeats the category names without adding a consequence.

## Revision

> We distinguish three evidence states for deployment decisions. In the technical state, the system has passed reproducibility and failure-recovery tests but has not been evaluated with patient data; it may proceed to controlled data-pipeline testing, but no clinical claim is permitted. In the retrospective clinical state, performance has been evaluated on a held-out historical cohort; the system may proceed to a prospective silent study, but clinicians must not receive its output. In the prospective clinical state, performance and workflow effects have been evaluated prospectively in the intended setting; deployment may be considered subject to the study's limitations and local governance.

## Why the taxonomy stays

Deleting or merging the categories would erase a decision boundary. The skill should not optimize for fewer labels; it should remove labels only when they rename the same concept or do not change interpretation, evaluation, or action.

The Introduction may preview these states and the Conclusion may return to their deployment implication. That normal correspondence is not redundant if neither section reproduces the full definitions.
