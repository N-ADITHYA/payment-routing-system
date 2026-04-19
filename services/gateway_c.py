import random
import asyncio
import time

async def process_payment(payment_id: str):
    start = time.time()

    await asyncio.sleep(random.uniform(0.2, 1))

    if random.random() < 0.5:
        return {
            "status": "SUCCESS",
            "gateway": "C",
            "latency": time.time() - start
        }
    else:
        raise Exception("Gateway C random failure")