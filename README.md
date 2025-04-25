# Biostat821 Final Project
Biostat821 — Qianyu Zhu & Alicia Wang

---

# Biomedical Unit Conversion Library — `BioMed-Unit`

## Project Overview
**Name**: BioMed-Unit <br />
**Goal**: Provide a Python library offering comprehensive biomedical, clinical, nutritional, and financial unit conversions, along with lightweight medical calculators.

---

## Core Features

### 1. Unit Conversion
Conversion between common biomedical and physical units:
- **Concentrations**:  
  - Glucose: `mg/dL` ↔ `mmol/L`
  - Cholesterol: `mg/dL` ↔ `mmol/L`
  - Creatinine: `mg/dL` ↔ `µmol/L`
- **Weight**: `kg` ↔ `lb`
- **Volume**: `mL` ↔ `L`
- **Temperature**: `°C` ↔ `°F`
- **Length**: `cm` ↔ `inch`

### 2. Time Calculations
- Birthdate → Age
- Year ↔ Month ↔ Days conversions

### 3. Clinical Calculators
- **BMI** (Body Mass Index)
- **BSA** (Body Surface Area — Mosteller formula)
- **Dose Calculations** (mg/kg, mg/m²)
- **Creatinine Clearance** (Cockcroft-Gault formula)

### 4. Nutrition Conversions
- Calories ↔ Kilojoules
- Macronutrient (% of carbs, fats, proteins)
- Daily kcal per meal calculator


---

## Testing Plan

- Use `pytest`
- Full unit test coverage for all converters
- Check for edge cases and invalid inputs
- Lint with `ruff`
- Type checking with `mypy`
- Optional GitHub Actions CI workflow

---

## Code Organization
821_final_qz141_zw292 <br />├── Converters <br />│ ├── init.py │ ├── unit_conversion.py │ ├── time_conversion.py │ ├── clinical_conversion.py │ ├── nutrition_conversion.py │ ├── finance_conversion.py │ ├── ConverterTests/ │ ├── init.py │ └── test_converters.py │ ├── .pytest.ini ├── README.md └── requirements.txt


---

## Task Breakdown

| Member | Task |
|--------|------|
| Alicia Wang | Implement UnitConverter, TimeConverter, and their tests |
| Qianyu Zhu | Calculators for BMI, BSA, EGFR, drug dosage, and tests|
| Both | Code review, documentation, style consistency, finalize README |

---

## Why It's a Good Final Project

- **Scope is modular and scalable** — clear responsibilities, easy testing.
- **Emphasis on best practices** — style consistency, testing, documentation, clean project structure.
- **Real-world application** — healthcare professionals and researchers can directly benefit from unit conversions and calculators.
- **Well-organized architecture** — easy to expand with new conversions later.

---
