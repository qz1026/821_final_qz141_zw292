"""
BMI (Body Mass Index) Calculator.

This module provides a function to calculate BMI given weight in kilograms
and height in centimeters. Includes basic error handling for invalid inputs.
"""

def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    """
    Calculate Body Mass Index (BMI).

    Parameters:
        weight_kg (float): Weight of the individual in kilograms. Must be > 0.
        height_cm (float): Height of the individual in centimeters. Must be > 0.

    Returns:
        float: The calculated BMI value, rounded to 2 decimal places.

    Raises:
        ValueError: If either weight_kg or height_cm is non-positive.
    """
    if weight_kg <= 0:
        raise ValueError("Weight must be a positive number (kg).")
    if height_cm <= 0:
        raise ValueError("Height must be a positive number (cm).")

    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)