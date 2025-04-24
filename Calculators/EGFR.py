"""
eGFR (Estimated Glomerular Filtration Rate) Calculator Module.

Uses a simplified MDRD formula to estimate kidney function.
"""

def calculate_egfr_mdrd(
    scr_mg_dl: float,
    age_years: int,
    sex: str,
    race: str
) -> float:
    """
    Calculate eGFR using the simplified MDRD formula.

    Parameters:
        scr_mg_dl (float): Serum creatinine in mg/dL. Must be > 0.
        age_years (int): Age in years. Must be > 0.
        sex (str): 'male' or 'female'.
        race (str): 'black' or 'non-black'.

    Returns:
        float: Estimated GFR, rounded to 2 decimal places.

    Raises:
        ValueError: For invalid or missing inputs.
    """
    if scr_mg_dl <= 0:
        raise ValueError("Serum creatinine must be a positive number.")
    if age_years <= 0:
        raise ValueError("Age must be a positive integer.")

    sex = sex.lower()
    race = race.lower()

    if sex not in {"male", "female"}:
        raise ValueError("Sex must be 'male' or 'female'.")
    if race not in {"black", "non-black"}:
        raise ValueError("Race must be 'black' or 'non-black'.")

    egfr = 175 * (scr_mg_dl ** -1.154) * (age_years ** -0.203)

    if sex == "female":
        egfr *= 0.742
    if race == "black":
        egfr *= 1.212

    return round(egfr, 2)