import random
import asyncio
import time

async def process_payment(payment_id: str):
    start = time.time()

    await asyncio.sleep(0.5)

    r = random.random()

    if r < 0.6:
        return {
            "status": "SUCCESS",
            "gateway": "A",
            "latency": time.time() - start
        }
    elif r < 0.85:
        return {
            "status": "FAILED",
            "gateway": "A",
            "latency": time.time() - start
        }
    else:
        await asyncio.sleep(2)
        raise asyncio.TimeoutError("Gateway A timeout")