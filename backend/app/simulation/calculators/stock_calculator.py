from typing import Tuple, List, Dict


def simulate_stock(months: int, initial: float, monthly: float) -> Tuple[List[float], Dict]:
    # 아주 단순한 placeholder: 월 0.6% 기대수익률 가정
    rate = 0.006
    values: List[float] = []
    balance = initial
    for _ in range(months):
        balance = balance * (1 + rate) + monthly
        values.append(round(balance, 2))
    metrics = {"cagr": 0.075, "mdd": -0.15}
    return values, metrics



