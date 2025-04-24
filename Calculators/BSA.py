"""
BSA (Body Surface Area) Calculator Module.

Supports two commonly used formulas:
- DuBois and DuBois
- Mosteller
"""

def calculate_bsa(weight_kg: float, height_cm: float, method: str = "mosteller") -> float:
    """
    Calculate Body Surface Area (BSA) in square meters.

    Parameters:
        weight_kg (float): Weight in kilograms. Must be > 0.
        height_cm (float): Height in centimeters. Must be > 0.
        method (str): Formula to use. Options are 'mosteller' (default) or 'dubois'.

    Returns:
        float: BSA in square meters, rounded to 2 decimal places.

    Raises:
        ValueError: If inputs are invalid or unsupported method is specified.
    """
    if weight_kg <= 0:
        raise ValueError("Weight must be a positive number.")
    if height_cm <= 0:
        raise ValueError("Height must be a positive number.")

    method = method.lower()

    if method == "mosteller":
        bsa = (weight_kg * height_cm / 3600) ** 0.5
    elif method == "dubois":
        bsa = 0.007184 * (weight_kg ** 0.425) * (height_cm ** 0.725)
    else:
        raise ValueError("Unsupported method. Choose 'mosteller' or 'dubois'.")

    return round(bsa, 2)