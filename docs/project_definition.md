# Ethical AI Use Case & Impact Assessment (Digital Ethics + Cognitive Architecture)

### Project overview

Real AI work is judged as much by *reasoning and safeguards* as by the prototype itself.

This project asks students to ship a GitHub repo that includes:

- a clear **problem framing** and **decision boundary**
- an **ethical impact assessment** with mitigations
- a lightweight prototype or simulation
- documentation that makes intent, limitations, and failure modes explicit

### Nexus alignment

- **Primary domains:** Digital Ethics, Cognitive Architecture
- **Secondary domains:** Human-Computer Interaction, Systems Thinking

### Student-facing learning outcomes

By the end, students should be able to:

- define an AI-assisted decision scenario with explicit scope and constraints
- identify stakeholders, harms, and risk pathways
- propose and justify mitigations (human-in-the-loop, thresholds, fallback plans)
- document intended use, non-use, and limitations in a reviewable way
- ship a repo that communicates tradeoffs clearly to a non-author reviewer

---

### Scenario options (choose one)

Pick **one scenario** and keep it realistic. The goal is not a big model, it is a credible system proposal with evidence.

1. **Student support triage assistant**
    - Inputs: student ticket text + metadata
    - Output: recommended category and priority + suggested response template
2. **Admissions or scholarship screening support** (assistive only)
    - Inputs: structured application fields
    - Output: completeness checks + risk flags + reviewer checklist
3. **Healthcare administration workflow assistant**
    - Inputs: operational metrics, scheduling constraints
    - Output: recommendations with constraints and explanations
4. **Academic integrity / policy guidance assistant**
    - Inputs: policy text + scenario
    - Output: guidance + citations to policy sections + uncertainty flags

### Definition of done (MVP)

A repo is “done” when:

- the decision scope is clear (what it does and does not do)
- risks are documented with specific mitigations
- a reviewer can run a demo (even if minimal)
- limitations and failure modes are explicit

---

### Required deliverables (evidence artifacts)

**1) [`README.md`](http://README.md)**

- What problem is being addressed
- Who the users are
- What the system outputs
- What it does **not** do
- How to run the demo

**2) `docs/[problem-brief.md](http://problem-brief.md)`**

- Context and stakeholders
- Decision being supported
- Constraints, assumptions, success criteria

**3) `docs/[ethical-impact-assessment.md](http://ethical-impact-assessment.md)`**

- Stakeholders and harms
- Risk register (risk → likelihood → impact)
- Mitigation plan (technical + process)

**4) `docs/[system-card.md](http://system-card.md)` (or model-card)**

- Intended use, non-use
- Data assumptions
- Limitations
- Monitoring / review plan

**5) Prototype / simulation**

- A minimal script, notebook, or small app that demonstrates the workflow.
- Must include at least 3 test cases: normal case, edge case, failure case.

**6) `docs/[user-experience-notes.md](http://user-experience-notes.md)`**

- User journey
- How uncertainty is communicated
- “Safe defaults” and fallback behaviors

---

### GitHub workflow requirements (graded behaviors)

- **Issues**
    - at least 6 issues
    - include at least 2 issues tagged `risk`
    - include at least 1 issue tagged `mitigation`
- **Pull Requests**
    - at least 2 PRs
    - at least 1 PR must be documentation-focused
    - each PR includes: summary, how to test, and what changed
- **Discussion / decision log**
    - use GitHub Discussions or a dedicated issue thread to document ethical tradeoffs
- **Release tags**
    - `v0.1` = scenario + docs skeleton + runnable demo
    - `v1.0` = complete evidence package + mitigations + tests/cases

---

### Suggested repo structure (complete)

```
.
├── [README.md](http://README.md)
├── docs/
│   ├── [problem-brief.md](http://problem-brief.md)
│   ├── [ethical-impact-assessment.md](http://ethical-impact-assessment.md)
│   ├── [system-card.md](http://system-card.md)
│   ├── [user-experience-notes.md](http://user-experience-notes.md)
│   └── [decision-log.md](http://decision-log.md)            # optional
├── src/
│   ├── [demo.py](http://demo.py)                    # or app entry point
│   └── helpers/
├── tests/
│   ├── test_[cases.md](http://cases.md)              # or automated tests
│   └── test_demo_[behavior.py](http://behavior.py)      # optional
├── examples/
│   ├── case_normal.json
│   ├── case_edge.json
│   └── case_failure.json
├── requirements.txt               # or environment.yml
├── .gitignore
└── assets/
    └── diagrams/
```

---

### Evaluation rubric (simple)

- **Problem framing & boundaries (25%)**: scope and non-scope are explicit.
- **Ethical rigor (25%)**: risks and mitigations are specific and plausible.
- **Usability & safety (25%)**: UX communicates uncertainty and defaults safely.
- **Evidence quality (25%)**: repo is reviewable, runnable, and well documented.

---

### Stretch goals

- Add a bias/error-mode checklist and show how it was applied.
- Add a red-team script (prompting/abuse cases) and mitigations.
- Add a human-in-the-loop diagram with escalation rules.
- Add basic automated tests for the demo behavior.

<aside>
🧾

**Portfolio note**: The strongest submission reads like a responsible system handoff: clear boundaries, explicit risks, and evidence that the team thought about failure.

</aside>