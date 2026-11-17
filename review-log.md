# Week 7 Review Log

Pull request: (paste the link)
AI reviewer used: CodeRabbit / `ai_review_sample.md` / other (say which, and why)
Date:

## 1. Task 1: Review findings

One row per finding. Write your own findings (source "me") BEFORE you read the AI's. Number them RV-01, RV-02 and so on. If you use `ai_review_sample.md`, keep its IDs and number your own from RV-11.

- **Class:** Bug hit (a real defect), Valid suggestion (correct and worth doing, but not a defect) or Noise (wrong, irrelevant, out of scope or not worth doing).
- **Label:** a Conventional Comments label: `issue (blocking)`, `issue (non-blocking)`, `suggestion (non-blocking)`, `nitpick (non-blocking)` or `question`.
- **Decision:** Fix now, Register as debt, or Reject.

| ID | Source (me / AI / partner) | Line | Finding in one line | Class | Label | Decision | Reason (name the PS or US where one applies) |
|---|---|---|---|---|---|---|---|
| RV-01 | | | | | | | |

Summary:
- AI comments: ___ in total; ___ Bug hit, ___ Valid suggestion, ___ Noise.
- Findings only you (or your partner) made:
- AI comments you rejected, and what you needed to know to reject them:

## 2. Task 2: Resolve

Behaviour changes (one row per change; the test must fail before the fix and pass after it):

| Finding | Test you added | Failed before the fix? | Passes after? | Commit |
|---|---|---|---|---|
| | | | | |

Refactoring (no behaviour change):

- AI tool and model:
- Prompt used (paste it):
- What you accepted, changed or rejected from the AI's refactoring:

| Measure | Before refactoring | After refactoring |
|---|---|---|
| `radon cc usage_report.py -s -a`: highest function complexity and rank | | |
| `radon cc`: average complexity | | |
| `ruff check .` with the complexity gate (CI-14) | | |
| Tests passed / total | | |
| `equivalence_check.py`: differences | not applicable | |

- Link to the red run (complexity gate failing):
- Link to the green run after refactoring:

## 3. Reflection (100-150 words)

The pipeline was green before anyone reviewed this code. What did review find that the gates could not, and which of those findings came from a person and not from the AI?
