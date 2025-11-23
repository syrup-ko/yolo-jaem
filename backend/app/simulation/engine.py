from typing import List, Dict
from .calculators.stock_calculator import simulate_stock
from .calculators.real_estate_calculator import simulate_real_estate
from .calculators.deposit_calculator import simulate_deposit


class SimulationEngine:
    def run(self, assets: List[str], years: int, initial_capital: float, monthly_contribution: float) -> Dict:
        timeline_len = years * 12
        dates = [f"M{i+1}" for i in range(timeline_len)]
        asset_series = []
        for a in assets:
            if a.lower() == "stock":
                values, metrics = simulate_stock(timeline_len, initial_capital, monthly_contribution)
            elif a.lower() == "realestate":
                values, metrics = simulate_real_estate(timeline_len, initial_capital, monthly_contribution)
            else:
                values, metrics = simulate_deposit(timeline_len, initial_capital, monthly_contribution)
            asset_series.append({"name": a, "values": values, **metrics})
        timeline = [{"date": d, "total": float(sum(vals))} for d, vals in zip(dates, zip(*[s["values"] for s in asset_series]))]
        return {"timeline": timeline, "assets": asset_series}



