def diff_tariffs(previous, current):
    previous_ids = {item["tariff_id"] for item in previous if "tariff_id" in item}
    return [item for item in current if item.get("tariff_id") not in previous_ids]
