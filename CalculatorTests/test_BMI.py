"""
Tests for the BMI calculator.
"""

import pytest
from Calculators.BMI import calculate_bmi

def test_bmi_typical_values():
    assert calculate_bmi(70, 175) == 22.86
    assert calculate_bmi(60, 160) == 23.44
    assert calculate_bmi(90, 180) == 27.78


@pytest.mark.parametrize("weight, height", [
    (0, 170),
    (-5, 170),
    (70, 0),
    (70, -150),
])
def test_bmi_invalid_inputs(weight, height):
    with pytest.raises(ValueError):
        calculate_bmi(weight, height)