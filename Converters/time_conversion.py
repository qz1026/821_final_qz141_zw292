"""
time_conversion.py

Handles time-related conversions.
"""

from datetime import datetime
from typing import Optional

class TimeConverter:
    def date_to_age(self, birthdate: str, reference_date: Optional[str] = None) -> int:
        """Convert a birthdate (YYYY-MM-DD) into age in years."""
        birth = datetime.strptime(birthdate, "%Y-%m-%d")
        today = datetime.strptime(reference_date, "%Y-%m-%d") if reference_date else datetime.today()
        age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
        return age

    def year_to_month(self, years: float) -> float:
        return round(years * 12, 1)

    def month_to_year(self, months: float) -> float:
        return round(months / 12, 2)

    def days_to_year(self, days: float) -> float:
        return round(days / 365.25, 2)

    def year_to_days(self, years: float) -> float:
        return round(years * 365.25, 0)
