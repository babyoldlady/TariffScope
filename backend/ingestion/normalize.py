def normalize_tariff(row: dict) -> dict:
    return {
        "tariff_id": row.get("tariff_id", ""),
        "issuer": row.get("issuer", ""),
        "tariff_no": row.get("tariff_no", ""),
        "tariff_type": row.get("tariff_type", ""),
        "product_type": row.get("product_type", ""),
        "origin": row.get("origin", ""),
        "destination": row.get("destination", ""),
        "regulator": row.get("regulator", ""),
        "status": row.get("status", ""),
        "effective_yes_no": row.get("effective_yes_no", False),
    }
