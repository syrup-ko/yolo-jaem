from typing import List, Dict


async def get_supported_assets() -> List[str]:
    return ["Stock", "HYSA", "RealEstate"]


async def fetch_asset_timeseries(asset: str) -> Dict:
    # TODO: 외부 API 연동 및 정규화
    return {"asset": asset, "prices": []}



