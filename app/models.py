from pydantic import BaseModel
from datetime import datetime

class Quotation(BaseModel):
    id: int | None = None
    status: str
    opened_at: datetime
