def cagr(final_value: float, initial_value: float, years: int) -> float:
    if years <= 0 or initial_value <= 0:
        return 0.0
    return (final_value / initial_value) ** (1 / years) - 1



