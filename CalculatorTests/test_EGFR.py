"""
Tests for the eGFR calculator module.
"""

import pytest
from Calculators.EGFR import calculate_egfr_mdrd

def test_egfr_typical():
    result = calculate_egfr_mdrd(1.0, 50, "male", "non-black")
    assert round(result, 2) == 79.09  # Approximate expected value

    result = calculate_egfr_mdrd(1.0, 50, "female", "black")
    assert round(result, 2) == 71.13  # 80.5 * 0.742 * 1.212 ≈ 72.5


@pytest.mark.parametrize("scr, age", [
    (0, 50),
    (-1.0, 50),
    (1.0, 0),
])
def test_egfr_invalid_scr_or_age(scr, age):
    with pytest.raises(ValueError):
        calculate_egfr_mdrd(scr, age, "male", "black")


@pytest.mark.parametrize("sex", ["other", "", "MALEEE"])
def test_egfr_invalid_sex(sex):
    with pytest.raises(ValueError):
        calculate_egfr_mdrd(1.0, 50, sex, "black")


@pytest.mark.parametrize("race", ["asian", "", "whiteish"])
def test_egfr_invalid_race(race):
    with pytest.raises(ValueError):
        calculate_egfr_mdrd(1.0, 50, "male", race)