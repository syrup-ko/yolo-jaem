def calculate_mdd(values):
    peak = values[0] if values else 0
    max_drawdown = 0.0
    for v in values:
        if v > peak:
            peak = v
        drawdown = (v - peak) / peak if peak else 0
        if drawdown < max_drawdown:
            max_drawdown = drawdown
    return round(max_drawdown, 4)



