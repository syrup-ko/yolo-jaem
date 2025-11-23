from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import Integer, String, Float, DateTime
from datetime import datetime

Base = declarative_base()


class PricePoint(Base):
    __tablename__ = "price_points"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    asset: Mapped[str] = mapped_column(String, index=True)
    at: Mapped[datetime] = mapped_column(DateTime, index=True, default=datetime.utcnow)
    value: Mapped[float] = mapped_column(Float)



