idempotency_store = {}

def check_idempotency(key: str):
    return idempotency_store.get(key)

def save_idempotency(key: str, result: dict):
    idempotency_store[key] = result