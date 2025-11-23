from fastapi import APIRouter
from ...schemas.simulation_schema import SimulationRequest, SimulationResponse
from ...services.simulation_service import simulate_portfolio

router = APIRouter()


@router.post("/simulate", response_model=SimulationResponse)
async def simulate(req: SimulationRequest) -> SimulationResponse:
    return await simulate_portfolio(req)



