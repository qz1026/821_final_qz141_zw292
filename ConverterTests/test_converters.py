"""
test_converters.py

Tests for all converter classes.
"""
import pytest  # type: ignore

from Converters import UnitConverter, TimeConverter, ClinicalConverter, NutritionConverter

# Instantiate converters
uc = UnitConverter()
tc = TimeConverter()
cc = ClinicalConverter()
nc = NutritionConverter()

# --------------------------
# UnitConverter Tests
# --------------------------

def test_unit_glucose_mgdl_to_mmol():
    assert uc.convert(90, "mg/dL", "mmol/L") == 5.0

def test_unit_weight_lb_to_kg():
    assert uc.convert(150, "lb", "kg") == 68.04

def test_unit_temperature_f_to_c():
    assert uc.convert(98.6, "F", "C") == 37.0

def test_unit_length_inch_to_cm():
    assert uc.convert(72, "inch", "cm") == 182.88

def test_unit_invalid_conversion():
    with pytest.raises(ValueError):
        uc.convert(100, "foo", "bar")

# --------------------------
# TimeConverter Tests
# --------------------------

def test_time_date_to_age():
    assert tc.date_to_age("2000-01-01", reference_date="2025-01-01") == 25

def test_time_year_to_month():
    assert tc.year_to_month(2) == 24.0

def test_time_month_to_year():
    assert tc.month_to_year(18) == 1.5

def test_time_days_to_year():
    assert tc.days_to_year(730) == 2.0

def test_time_year_to_days():
    assert tc.year_to_days(2) == 730.0

# --------------------------
# ClinicalConverter Tests
# --------------------------

def test_clinical_bmi():
    assert cc.bmi(weight_kg=60, height_cm=165) == 22.04

def test_clinical_bsa_mosteller():
    assert cc.bsa_mosteller(weight_kg=60, height_cm=165) == 1.66

def test_clinical_dose_per_kg():
    assert cc.dose_per_kg(total_mg=600, weight_kg=60) == 10.0

def test_clinical_dose_per_m2():
    assert cc.dose_per_m2(total_mg=300, bsa_m2=1.5) == 200.0

def test_clinical_creatinine_clearance():
    assert cc.creatinine_clearance_cockcroft(age=30, weight_kg=70, serum_creatinine_mgdl=1.0, sex="M") == 106.94

# --------------------------
# NutritionConverter Tests
# --------------------------

def test_nutrition_kcal_to_kj():
    assert nc.kcal_to_kj(500) == 2092.0

def test_nutrition_kj_to_kcal():
    assert nc.kj_to_kcal(4184) == 1000.0

def test_nutrition_macros_percent():
    result = nc.macros_percent(carbs_g=200, fat_g=60, protein_g=100)
    assert result == {'carb_pct': 46.0, 'fat_pct': 31.0, 'protein_pct': 23.0}

def test_nutrition_kcal_per_meal():
    assert nc.kcal_per_meal(daily_kcal=2100, meals=3) == 700.0

