from typing import List


def generate_monthly_dates(months: int) -> List[str]:
    return [f"M{i+1}" for i in range(months)]



