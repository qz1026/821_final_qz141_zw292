"""
nutrition_conversion.py

Handles nutrition-related conversions.
"""

class NutritionConverter:
    def kcal_to_kj(self, kcal: float) -> float:
        return round(kcal * 4.184, 2)

    def kj_to_kcal(self, kj: float) -> float:
        return round(kj / 4.184, 2)

    def macros_percent(self, carbs_g: float, fat_g: float, protein_g: float) -> dict:
        total_kcal = carbs_g * 4 + fat_g * 9 + protein_g * 4
        return {
            "carb_pct": round((carbs_g * 4 / total_kcal) * 100, 1),
            "fat_pct": round((fat_g * 9 / total_kcal) * 100, 1),
            "protein_pct": round((protein_g * 4 / total_kcal) * 100, 1),
        }

    def kcal_per_meal(self, daily_kcal: float, meals: int = 3) -> float:
        return round(daily_kcal / meals, 1)
