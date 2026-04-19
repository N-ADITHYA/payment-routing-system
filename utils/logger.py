payment_logs = []

def log_payment(payment_id, gateway, status, latency):
    log = {
        "payment_id": payment_id,
        "gateway": gateway,
        "status": status,
        "latency": round(latency, 3)
    }

    payment_logs.append(log)

    print(log)