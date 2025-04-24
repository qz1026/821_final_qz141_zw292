# Biostat821_final
Biostat821 Qianyu Zhu &amp; Alicia Wang


# Biomedical Unit Conversion Library

## Project Overview
**Name**: 'BioMed-Unit'
**Goal**: This project aims to provide a Python library to convert between common biomedical units and perform lightweight medical calculations like BMI, body surface area, and eGFR.

---

## Core Features

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
| Alicia | Implement `glucose`, `cholesterol` conversions + write tests |
| Qianyu | Implement `BMI`, `BSA` calculators + write tests |
| Both | Review each other’s PRs, write README and usage examples |


---

## Why It's a Good Final Project

- The scope is flexible — MVP is small and focused, but easily extensible.
- It has simple functions that are ideal for PR feedback as well as tests.
- It is useful in real life as clinicians and researchers would actually use these.
