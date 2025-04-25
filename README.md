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
- **BSA** (Body Surface Area — DuBois & Mosteller formula)
- **Dose Calculations** (mg/kg, mg/m²)
- **EGFR** (MDRD formula)

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
821_final_qz141_zw292/ <br />
│ <br />
├── Converters/             # Contains all converter modules <br />
│   ├── __init__.py         <br />
│   ├── unit_conversion.py               # Unit conversion <br />
│   ├── time_conversion.py               # Time conversion <br />
│   ├── clinical_conversion.py           # Clinical conversion <br />
│   ├── nutritional_conversion.py        # Nutritional conversion <br />
│   └── finance_conversion.py            # Finance conversion <br />
│ <br />
├── ConverterTests/         # Unit tests for unit converter modules <br />
│   ├── __init__.py <br />
│   ├── test_converters.py <br />
│ <br />
├── Calculators/             # Contains all calculation modules <br />
│   ├── __init__.py          # Makes this a Python package <br />
│   ├── BMI.py               # BMI calculator <br />
│   ├── BSA.py               # BSA calculator <br />
│   ├── EGFR.py              # eGFR calculator <br />
│   └── Dose.py              # Drug dosage calculator <br />
│ <br />
├── CalculatorTests/         # Unit tests for calculator modules <br />
│   ├── __init__.py <br />
│   ├── test_BMI.py <br />
│   ├── test_BSA.py <br />
│   ├── test_EGFR.py  <br />
│   └── test_Dose.py <br />
│ <br />
├── README.md                # Project overview and instructions  <br />
└── requirements.txt         # Required packages  <br />

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
