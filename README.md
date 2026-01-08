# Student Workflow & Submission Guide

> [!IMPORTANT]
> **READ THIS FIRST**: Do not commit directly to the `main` branch of this repository.

This repository serves as the **template** for your project. To work on it, follow the standard GitHub workflow:

1.  **Fork** this repository to your own GitHub account (click the "Fork" button in the top right).
2.  **Clone** your forked repository to your local machine:
    ```bash
    git clone https://github.com/YOUR_USERNAME/bounded-by-design.git
    ```
3.  **Create a Branch** for your work. **Do not work on `main`**.
    ```bash
    git checkout -b feature/initial-setup
    ```
4.  **Work and Commit** your changes locally.
5.  **Push** your branch to your fork:
    ```bash
    git push -u origin feature/initial-setup
    ```
6.  **Open a Pull Request (PR)** on GitHub to merge your changes into your `main` branch (or submit as directed by your instructor).

---

# Ethical AI Use Case & Impact Assessment

## Project Overview
Real AI work is judged as much by *reasoning and safeguards* as by the prototype itself. 
This project challenges you to ship a GitHub repo that clearly communicates the intent, limitations, and failure modes of an AI-assisted decision scenario.

You will deliver:
- A clear **problem framing** and **decision boundary**
- An **ethical impact assessment** with mitigations
- A lightweight **prototype or simulation**
- Documentation of "intent" vs. "limitations"

## Scenario Options
Choose **one** of the following scenarios to base your project on. Keep it realistic; the goal is a credible system proposal, not a large model.

### 1. Student Support Triage Assistant
- **Inputs**: Student ticket text + metadata
- **Output**: Recommended category/priority + suggested response
- **Focus**: Triage efficiency vs. misclassification risks

### 2. Admissions or Scholarship Screening Support
- **Inputs**: Structured application fields
- **Output**: Completeness checks + risk flags + reviewer checklist
- **Focus**: Fairness, bias mitigation, and human-in-the-loop

### 3. Healthcare Administration Workflow Assistant
- **Inputs**: Operational metrics, scheduling constraints
- **Output**: Recommendations with constraints and explanations
- **Focus**: Operational safety and stakeholder constraints

### 4. Academic Integrity / Policy Guidance Assistant
- **Inputs**: Policy text + scenario
- **Output**: Guidance + citations + uncertainty flags
- **Focus**: Accuracy, citations, and handling ambiguity

## Definition of Done (MVP)
A repo is considered "done" when:
- The decision scope is clear (what it DOES and DOES NOT do).
- Risks are documented with specific mitigations.
- A reviewer can run a demo (even if minimal).
- Limitations and failure modes are explicitly stated.

## How to Run

### 1. Local Setup
Ensure you have Python installed.

1.  **Run the Demo**:
    ```bash
    python src/demo.py examples/case_normal.json
    ```
    Try other test cases: `examples/case_edge.json`, `examples/case_failure.json`.

### 2. Check Your Progress
We have provided a script to help you validate that your project structure meets the requirements.

1.  **Run Validation**:
    ```bash
    python scripts/validate_progress.py
    ```

### 3. Automated Validation (CI/CD)
Every time you push a commit or open a Pull Request, **GitHub Actions** will automatically run the validation script.
- **✅ Pass**: Structure is correct.
- **❌ Fail**: Missing required files or directories. Check the "Actions" tab.

## Required Deliverables

Your repository must include the following evidence artifacts (templates provided in `docs/`):

1.  **`README.md`** (This file, updated with your project specifics)
2.  **`docs/problem-brief.md`**: Context, decision support, and constraints.
3.  **`docs/ethical-impact-assessment.md`**: Stakeholders, risk register, and mitigation plan.
4.  **`docs/system-card.md`**: Intended use, non-use, limitations, and monitoring.
5.  **`docs/user-experience-notes.md`**: User journey, uncertainty communication, and fallbacks.
6.  **Prototype**: A working script (`src/demo.py`) with at least 3 test cases (normal, edge, failure).

## Project Structure
```
.
├── README.md
├── docs/
│   ├── problem-brief.md
│   ├── ethical-impact-assessment.md
│   ├── system-card.md
│   └── user-experience-notes.md
├── src/
│   └── demo.py
├── examples/
│   ├── case_normal.json
│   ├── case_edge.json
│   └── case_failure.json
├── scripts/
│   └── validate_progress.py
└── .github/
    └── workflows/
        └── evidence.yml
```
