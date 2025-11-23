from pydantic import BaseModel, Field, conlist
from typing import List, Optional


class SimulationRequest(BaseModel):
    assets: conlist(str, min_length=2)  # at least two assets
    durationYears: int = Field(ge=1, description="시뮬레이션 기간(년)")
    initialCapital: float = Field(ge=0)
    monthlyContribution: float = Field(ge=0)


class TimelinePoint(BaseModel):
    date: str
    total: float


class AssetSeries(BaseModel):
    name: str
    values: List[float]
    cagr: Optional[float] = None
    mdd: Optional[float] = None


class SimulationResponse(BaseModel):
    timeline: List[TimelinePoint]
    assets: List[AssetSeries]



