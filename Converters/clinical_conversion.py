"""
clinical_conversion.py

Handles clinical formula-based conversions and calculators.
"""

import math

class ClinicalConverter:
    def bmi(self, weight_kg: float, height_cm: float) -> float:
        height_m = height_cm / 100
        return round(weight_kg / (height_m ** 2), 2)

    def bsa_mosteller(self, weight_kg: float, height_cm: float) -> float:
        """Body Surface Area (m²) using Mosteller formula."""
        return round(math.sqrt((height_cm * weight_kg) / 3600), 2)

    def dose_per_kg(self, total_mg: float, weight_kg: float) -> float:
        return round(total_mg / weight_kg, 2)

    def dose_per_m2(self, total_mg: float, bsa_m2: float) -> float:
        return round(total_mg / bsa_m2, 2)

    def creatinine_clearance_cockcroft(self, age: int, weight_kg: float, serum_creatinine_mgdl: float, sex: str = "M") -> float:
        """Estimates creatinine clearance using Cockcroft-Gault formula."""
        sex_factor = 0.85 if sex.upper() == "F" else 1
        crcl = ((140 - age) * weight_kg) / (72 * serum_creatinine_mgdl) * sex_factor
        return round(crcl, 2)
