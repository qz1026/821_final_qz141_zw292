"""
unit_conversion.py

Handles biomedical and physical unit conversions.
"""

class UnitConverter:
    _conversion_factors = {
        # Concentrations
        ("mg/dL", "mmol/L"): 1/18.0,
        ("mmol/L", "mg/dL"): 18.0,
        ("mg/dL_chol", "mmol/L_chol"): 1/38.67,
        ("mmol/L_chol", "mg/dL_chol"): 38.67,
        ("mg/dL_crea", "µmol/L_crea"): 88.4,
        ("µmol/L_crea", "mg/dL_crea"): 1/88.4,
        
        # Weight
        ("lb", "kg"): 0.453592,
        ("kg", "lb"): 1/0.453592,

        # Length
        ("inch", "cm"): 2.54,
        ("cm", "inch"): 1/2.54,
        ("m", "cm"): 100,
        ("cm", "m"): 1/100,

        # Volume
        ("mL", "L"): 0.001,
        ("L", "mL"): 1000,

        # Mass
        ("g", "kg"): 0.001,
        ("kg", "g"): 1000,
    }

    def convert(self, value: float, from_unit: str, to_unit: str) -> float:
        if (from_unit, to_unit) == ("F", "C"):
            return round((value - 32) * 5/9, 2)
        elif (from_unit, to_unit) == ("C", "F"):
            return round((value * 9/5) + 32, 2)

        key = (from_unit, to_unit)
        if key not in self._conversion_factors:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} not supported.")
        
        return round(value * self._conversion_factors[key], 2)
