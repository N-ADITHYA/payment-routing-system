import asyncio
import time

async def process_payment(payment_id: str):
    start = time.time()

    await asyncio.sleep(0.86)

    return {
        "status": "SUCCESS",
        "gateway": "B",
        "latency": time.time() - start
    }