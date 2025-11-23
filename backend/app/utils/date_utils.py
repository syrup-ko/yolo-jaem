from datetime import datetime


def utcnow_str() -> str:
    return datetime.utcnow().isoformat()



