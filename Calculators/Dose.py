"""
Drug Dose Normalization Module.

Provides functions to normalize a total drug dose by body weight or surface area.
"""

def dose_per_kg(total_dose_mg: float, weight_kg: float) -> float:
    """
    Normalize a drug dose by body weight (mg/kg).

    Parameters:
        total_dose_mg (float): Total dose administered, in milligrams. Must be > 0.
        weight_kg (float): Patient's weight in kilograms. Must be > 0.

    Returns:
        float: Dose per kilogram (mg/kg), rounded to 2 decimal places.

    Raises:
        ValueError: If inputs are non-positive.
    """
    if total_dose_mg <= 0 or weight_kg <= 0:
        raise ValueError("Both total dose and weight must be positive values.")
    
    return round(total_dose_mg / weight_kg, 2)

def dose_per_bsa(total_dose_mg: float, bsa_m2: float) -> float:
    """
    Normalize a drug dose by body surface area (mg/m²).

    Parameters:
        total_dose_mg (float): Total dose administered, in milligrams. Must be > 0.
        bsa_m2 (float): Patient's body surface area in square meters. Must be > 0.

    Returns:
        float: Dose per square meter (mg/m²), rounded to 2 decimal places.

    Raises:
        ValueError: If inputs are non-positive.
    """
    if total_dose_mg <= 0 or bsa_m2 <= 0:
        raise ValueError("Both total dose and BSA must be positive values.")
    
    return round(total_dose_mg / bsa_m2, 2)