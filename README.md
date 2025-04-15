# Biostat821_final
Biostat821 Qianyu Zhu &amp; Alicia Wang


# Biomedical Unit Conversion Library – `biomed-units`

## Project Overview

**Name (example)**: `biomed-units`  
**Goal**: Provide a Python library (with optional CLI or web interface) to convert between common biomedical units and perform lightweight medical calculations like BMI, body surface area, and eGFR.

---

## Core Features (MVP)

### 1. Unit Conversion Functions
Each implemented as a clean, well-documented, and testable function.
Examples:
- **Glucose**: `mg/dL` ↔ `mmol/L`  
  > `glucose_mgdl_to_mmol(glucose_mgdl: float) -> float`
- **Cholesterol**: `mg/dL` ↔ `mmol/L`
- **Creatinine**: `mg/dL` ↔ `µmol/L`
- **HbA1c**: % ↔ mmol/mol

### 2. Biomedical Calculators
Helpful for clinicians and researchers.
- **BMI** (Body Mass Index): `calculate_bmi(weight_kg: float, height_cm: float) -> float`
- **BSA** (Body Surface Area) using DuBois or Mosteller formula
- **eGFR** calculators (e.g., MDRD or CKD-EPI, simplified for demo)
- **Unit-normalized drug dose calculator** (e.g., dose per kg or BSA)

---

## Testing Plan

- Use `pytest`
- 100% coverage for all converters
- Include parameterized tests for edge cases (e.g., zero, negatives, round-trip conversion)
- GitHub Actions + `ruff` lint + coverage badge

---

## Code Organization Example

```
biomed_units/
│
├── converters/
│   ├── glucose.py
│   ├── cholesterol.py
│   ├── creatinine.py
│   └── __init__.py
│
├── calculators/
│   ├── bmi.py
│   ├── bsa.py
│   └── egfr.py
│
├── cli/
│   └── main.py  (optional)
│
├── tests/
│   ├── test_glucose.py
│   ├── test_bmi.py
│   └── ...
│
├── pyproject.toml
├── README.md
└── LICENSE
```

---

## Task Breakdown for 2–3 Person Team

| Member | Task |
|--------|------|
| Person A | Implement `glucose`, `cholesterol` conversions + write tests |
| Person B | Implement `BMI`, `BSA` calculators + write tests |
| All | Review each other’s PRs, write README and usage examples |


---

## Why It's a Good Final Project

- **Scope is flexible** — MVP is small and focused, but easily extensible.
- **Great for code review** — simple pure functions are ideal for PR feedback.
- **Tests are natural** — deterministic inputs/outputs.
- **Useful in real life** — clinicians and researchers actually use these.
- **Frontend optional** — CLI or Flask/Streamlit stretch goals.
