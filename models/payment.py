from pydantic import BaseModel

class PaymentResponse(BaseModel):
    payment_id: str
    result: dict