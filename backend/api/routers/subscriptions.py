from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SubscriptionCreate(BaseModel):
    issuer: str
    email: str | None = None
    tariff_type: str | None = None
    product_type: str | None = None
    state: str | None = None

@router.post("/")
def create_subscription(payload: SubscriptionCreate):
    return {"created": True, "subscription": payload.model_dump()}
