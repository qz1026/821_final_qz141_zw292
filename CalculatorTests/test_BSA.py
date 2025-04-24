"""
Tests for the BSA calculator module.
"""

import pytest
from Calculators.BSA import calculate_bsa

def test_bsa_mosteller():
    assert calculate_bsa(70, 175) == 1.84
    assert calculate_bsa(60, 160) == 1.63


def test_bsa_dubois():
    assert calculate_bsa(70, 175, method="dubois") == 1.85
    assert calculate_bsa(60, 160, method="dubois") == 1.62


@pytest.mark.parametrize("weight, height", [
    (0, 170),
    (-5, 170),
    (70, 0),
    (70, -150),
])
def test_bsa_invalid_inputs(weight, height):
    with pytest.raises(ValueError):
        calculate_bsa(weight, height)


def test_bsa_invalid_method():
    with pytest.raises(ValueError):
        calculate_bsa(70, 175, method="weirdmethod")