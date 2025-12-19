from enum import Enum
from pydantic import BaseModel
from datetime import datetime


class QuotationStatus(str, Enum):
    WAITING_SUPPLIER = "WAITING_SUPPLIER"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class Quotation(BaseModel):
    id: int | None = None
    status: QuotationStatus
    opened_at: datetime