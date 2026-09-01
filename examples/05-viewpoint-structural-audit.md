# Long Viewpoint: document-level structural audit

**Case type:** English Viewpoint / framework paper
**Source status:** Synthetic demonstration
**Input profile:** 30 pages, approximately 9,800 words, nine main sections
**Goal:** Reduce cross-section semantic redundancy before line editing.

This example reports the complete audit and revision plan for a synthetic manuscript. Short extracts stand in for the full 30-page input so the repository does not ship a deliberately repetitive 10,000-word file.

## Representative input

### Abstract

> Self-checking can improve the internal consistency of a clinical language model's output, but it cannot establish clinical validity. We propose a verification–validation boundary to preserve this distinction.

### Introduction

> Internal checking and external validation answer different questions. A model may repeatedly verify its own output, yet these checks cannot determine whether the output is fit for clinical use.

### Five limits of self-verification

> The central limitation is therefore not the absence of checking, but the absence of independent evidence. Self-verification may support internal reliability, but it cannot establish validity in a target population.

### The two-gate model

> We distinguish an output gate from a use-case gate. The output gate concerns bounded self-verification. The use-case gate concerns external clinical validation. Passing the output gate cannot substitute for passing the use-case gate.

### Evidence states and action classes

> Internally checked outputs occupy a verification state, whereas independently evaluated systems occupy a validation state. No internal mechanism can move a system from the first state to the second.

### Governance

> The governance task is not to prohibit self-verification, but to prevent it from being misclassified as clinical validation. Internal reassurance cannot substitute for independent evidence.

### Conclusion

> Self-verification is useful, but it is not clinical validation. Clinical fitness requires independent evaluation in the intended population and setting.

## 1. One-sentence thesis

Self-verification can improve output-level quality control, but claims about clinical fitness require independent evaluation in the intended use context.

## 2. Thesis-recurrence map

| Location | Restatement | Analytical increment | Decision |
| --- | --- | --- | --- |
| Abstract | self-checking ≠ clinical validity | States the contribution | Keep, shorten |
| Introduction | internal checking ≠ fitness for use | Defines the problem | Keep |
| Five limits | checking lacks independent evidence | No new evidence or boundary in the quoted passage | Merge into the specific limits |
| Two-gate model | output gate ≠ use-case gate | Adds an operational sequence | Keep |
| Evidence states | verification state ≠ validation state | Relabels the same distinction without a new decision rule | Remove the state layer |
| Governance | do not misclassify checking as validation | Adds an institutional consequence | Keep the consequence; delete the repeated proof |
| Conclusion | self-verification ≠ clinical validation | Necessary closing echo | Keep in one sentence |

The manuscript needs the thesis in the Abstract, Introduction, and Conclusion. The problem is not recurrence alone; it is the four intervening restatements that add labels but little analysis.

## 3. Framework inventory

| Label family | Terms used | Function | Recommendation |
| --- | --- | --- | --- |
| Core distinction | verification–validation boundary | Names the thesis | Keep |
| Process | output gate / use-case gate | Connects evidence to a decision sequence | Keep |
| Status | verification state / validation state | Duplicates the boundary | Delete |
| Risk | five limits / five ethical risks | Partly overlapping lists | Combine around consequences |
| Governance | four action classes / four governance levels | Both allocate actions by evidence | Use one action matrix |

Stable vocabulary after compression: **verification**, **validation**, **output gate**, and **use-case gate**. “State,” “tier,” and “governance level” are removed unless a later section assigns them a distinct decision consequence.

## 4. One job for each section

| Section | Unique job after revision |
| --- | --- |
| Abstract | State the problem, distinction, operational proposal, and implication |
| Introduction | Show why internal checks are being mistaken for clinical evidence |
| Epistemic limits | Explain where self-verification fails and under what conditions |
| Two-gate model | Convert the distinction into an evaluation sequence |
| Governance | Assign actions and claims to the evidence available at each gate |
| Discussion | Compare the model with alternatives and identify failure conditions |
| Conclusion | State the practical implication once |

The original “evidence states” section has no unique job and should be absorbed into the two-gate model. Ethical risks belong with the decisions they affect rather than in a second parallel taxonomy.

## 5. Compression plan

1. Keep the Introduction's definition of the verification–validation boundary.
2. Replace the repeated opening and closing claims in the “five limits” section with one transition into the actual limits.
3. Retain the two gates because they specify an evaluation sequence.
4. Delete the evidence-state taxonomy; map any useful sentences to the corresponding gate.
5. Merge action classes and governance levels into one matrix: available evidence × permitted claim or action.
6. Rewrite the Discussion around boundary conditions, competing frameworks, and cases in which an external study still fails to validate the intended use.
7. Keep one sentence of thesis correspondence in the Conclusion.

Estimated target: 6,500–7,200 words. This is a planning range, not a rule. The final length depends on how much distinct evidence, comparison, and operational detail the full manuscript contains.

## 6. Sample compressed passage

### Before

> The governance task is not to prohibit self-verification, but to prevent it from being misclassified as clinical validation. This distinction is important because self-verification is an internal process, whereas clinical validation requires external evidence. No internal mechanism can independently move a system from an internally checked state to an externally validated state. Thus, internal reassurance cannot substitute for independent evidence of clinical fitness.

### After

> Governance should tie permissible claims to the evidence available at each gate. Passing the output gate permits a claim that specified internal checks were completed; only independent evaluation at the use-case gate can support a claim of clinical fitness.

The revision keeps the governance consequence and removes a fourth proof of the paper's central distinction.

## 7. What must not be deleted

- the operational difference between the two gates
- definitions required to interpret the framework
- any Methods or Results detail in an empirical version of the paper
- limitations, failure conditions, and competing explanations
- concise correspondence among Abstract, Introduction, and Conclusion

## Expected outcome

The manuscript becomes shorter because redundant claims and labels are merged, not because academic structure is mechanically stripped. The remaining framework has fewer names but clearer decision consequences.
