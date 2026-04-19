from fastapi import APIRouter, Header
import uuid

from services.router import route_payment
from services.idempotency import check_idempotency, save_idempotency

router = APIRouter()


@router.post("/pay")
async def pay(idempotency_key: str = Header(default=None)):
    if not idempotency_key:
        return {"error": "Idempotency-Key header required"}

    # Check duplicate
    existing = check_idempotency(idempotency_key)
    if existing:
        return {
            "message": "Duplicate request",
            "data": existing
        }

    payment_id = str(uuid.uuid4())

    result = await route_payment(payment_id)

    response = {
        "payment_id": payment_id,
        "result": result
    }

    save_idempotency(idempotency_key, response)

    return response