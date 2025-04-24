"""
Tests for the dose normalization module.
"""

import pytest
from Calculators.Dose import dose_per_kg, dose_per_bsa

def test_dose_per_kg_typical():
    assert dose_per_kg(500, 50) == 10.0
    assert dose_per_kg(200, 80) == 2.5


def test_dose_per_bsa_typical():
    assert dose_per_bsa(300, 1.5) == 200.0
    assert dose_per_bsa(600, 2.0) == 300.0


@pytest.mark.parametrize("dose, weight", [
    (0, 60),
    (-5, 60),
    (100, 0),
    (100, -50),
])
def test_dose_per_kg_invalid(dose, weight):
    with pytest.raises(ValueError):
        dose_per_kg(dose, weight)


@pytest.mark.parametrize("dose, bsa", [
    (0, 1.5),
    (-100, 1.5),
    (300, 0),
    (300, -2),
])
def test_dose_per_bsa_invalid(dose, bsa):
    with pytest.raises(ValueError):
        dose_per_bsa(dose, bsa)