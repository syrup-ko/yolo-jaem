from typing import List
from sqlalchemy.orm import Session
from .models import PricePoint


def save_price_points(db: Session, points: List[PricePoint]) -> None:
    db.add_all(points)
    db.commit()


def get_asset_points(db: Session, asset: str, limit: int = 1000) -> List[PricePoint]:
    return db.query(PricePoint).filter(PricePoint.asset == asset).order_by(PricePoint.at).limit(limit).all()



