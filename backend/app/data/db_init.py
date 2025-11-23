from sqlalchemy import create_engine
from .models import Base
from ..core.config import settings


def init_db() -> None:
    engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
    Base.metadata.create_all(bind=engine)



