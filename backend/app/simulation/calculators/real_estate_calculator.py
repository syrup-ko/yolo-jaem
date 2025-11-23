from typing import Tuple, List, Dict


def simulate_real_estate(months: int, initial: float, monthly: float) -> Tuple[List[float], Dict]:
    # placeholder: 월 0.4% 기대상승 + 월세수익(월 납입액의 20%) 가정
    rate = 0.004
    rent_yield_ratio = 0.2
    values: List[float] = []
    balance = initial
    for _ in range(months):
        balance = balance * (1 + rate) + monthly + monthly * rent_yield_ratio
        values.append(round(balance, 2))
    metrics = {"cagr": 0.055, "mdd": -0.1}
    return values, metrics



