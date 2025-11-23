from ..schemas.simulation_schema import SimulationRequest, SimulationResponse, AssetSeries, TimelinePoint
from ..simulation.engine import SimulationEngine


async def simulate_portfolio(req: SimulationRequest) -> SimulationResponse:
    engine = SimulationEngine()
    result = engine.run(
        assets=req.assets,
        years=req.durationYears,
        initial_capital=req.initialCapital,
        monthly_contribution=req.monthlyContribution,
    )
    timeline = [TimelinePoint(date=p["date"], total=p["total"]) for p in result["timeline"]]
    series = [AssetSeries(name=a["name"], values=a["values"], cagr=a.get("cagr"), mdd=a.get("mdd")) for a in result["assets"]]
    return SimulationResponse(timeline=timeline, assets=series)



