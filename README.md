# AI Student Career Recommendation System

A console-based Artificial Intelligence micro project that recommends suitable career options using a CSP-style filter and rule-based inference with forward chaining and backward chaining.

## Features

- Accepts student profile facts as comma-separated input.
- Uses IF-THEN rules to infer possible careers through forward chaining.
- Uses backward chaining to verify a selected career goal.
- Applies CSP-style filtering to keep career options supported by the profile facts.
- Displays recommendations and goal-verification results.

## Technologies Used

- Python 3
- Visual Studio Code or any Python editor
- Command Prompt / Terminal

## Career Rules

| Required facts | Recommended career |
|---|---|
| `interest_ai`, `strong_math`, `programming` | AI/ML Engineer |
| `interest_data`, `strong_math`, `analytical` | Data Analyst |
| `programming`, `problem_solving`, `interest_software` | Software Developer |
| `networking`, `security_interest`, `problem_solving` | Cybersecurity Analyst |

## How to Run

1. Install Python 3.
2. Download or clone this repository.
3. Open the project folder in a terminal.
4. Run:

```bash
python main.py
```

5. Enter facts separated by commas when prompted.

## Example

Input:

```text
interest_ai, strong_math, programming
```

Expected output:

```text
AI Student Career Recommendation System
Enter facts separated by commas.
Examples: interest_ai, strong_math, programming
Student facts: interest_ai, strong_math, programming

Recommended careers:
- AI/ML Engineer
  Goal verified: True
```

## Project Method

- **CSP:** Represents career selection using profile variables, domains, and constraints.
- **Forward chaining:** Starts with known student facts and applies matching rules to infer careers.
- **Backward chaining:** Starts with a career goal and checks whether its required facts are available.

## Note

This is an educational prototype. Its recommendations are based only on the rules included in the program and are not a final or guaranteed career decision.

## Project Report

See `AI_Student_Career_Recommendation_System_Report.pdf` for the micro project report.
