import asyncio
from services import gateway_a, gateway_b, gateway_c
from utils.logger import log_payment

async def route_payment(payment_id: str):

    gateways = [
        gateway_a.process_payment,
        gateway_b.process_payment,
        gateway_c.process_payment
    ]

    for gateway in gateways:
        try:
            result = await asyncio.wait_for(gateway(payment_id), timeout=1)

            log_payment(
                payment_id,
                result["gateway"],
                result["status"],
                result["latency"]
            )

            if result["status"] == "SUCCESS":
                return result

        except asyncio.TimeoutError:
            print(f"{gateway.__name__} timed out")
        except Exception as e:
            print(f"{gateway.__name__} failed: {e}")

    return {"status": "FAILED", "reason": "All gateways failed"}