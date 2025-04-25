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
821_final_qz141_zw292/
│
├── Converters/             # Contains all converter modules
│   ├── __init__.py         
│   ├── unit_conversion.py               # Unit conversion
│   ├── time_conversion.py               # Time conversion
│   ├── clinical_conversion.py           # Clinical conversion
│   ├── nutritional_conversion.py        # Nutritional conversion
│   └── finance_conversion.py            # Finance conversion
│
├── ConverterTests/         # Unit tests for unit converter modules
│   ├── __init__.py
│   ├── test_converters.py
│
├── Calculators/             # Contains all calculation modules
│   ├── __init__.py          # Makes this a Python package
│   ├── BMI.py               # BMI calculator
│   ├── BSA.py               # BSA calculator
│   ├── EGFR.py              # eGFR calculator
│   └── Dose.py              # Drug dosage calculator
│
├── CalculatorTests/         # Unit tests for calculator modules
│   ├── __init__.py
│   ├── test_BMI.py
│   ├── test_BSA.py
│   ├── test_EGFR.py 
│   └── test_Dose.py
│
├── README.md                # Project overview and instructions
└── requirements.txt         # Required packages

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
