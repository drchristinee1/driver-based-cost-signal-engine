from drivers.normalizer import normalize_service_metrics
from drivers.baseline import compare_to_baseline

THRESHOLD_PERCENT = 25.0

def run_driver_detection(service="all"):
    normalized = normalize_service_metrics(service=service)
    compared = compare_to_baseline(normalized)

    alerts = []

    for row in compared:
        if row["delta_percent"] >= THRESHOLD_PERCENT:
            row["status"] = "ALERT"
            alerts.append(row)

    for item in alerts:
        print(
            f"[{item['status']}] {item['resource']} | "
            f"{item['driver']} | {item['delta_percent']}%"
        )

    return alerts
