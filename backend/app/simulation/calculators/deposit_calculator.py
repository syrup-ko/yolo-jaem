from typing import Tuple, List, Dict


def simulate_deposit(months: int, initial: float, monthly: float) -> Tuple[List[float], Dict]:
    # HYSA/예금: 월 0.25% 단리 근사
    rate = 0.0025
    values: List[float] = []
    balance = initial
    for _ in range(months):
        balance = balance * (1 + rate) + monthly
        values.append(round(balance, 2))
    metrics = {"cagr": 0.03, "mdd": 0.0}
    return values, metrics



