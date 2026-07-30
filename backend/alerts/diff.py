def diff_tariffs(previous: list[dict], current: list[dict]) -> list[dict]:
    prev_ids = {x["tariff_id"] for x in previous if "tariff_id" in x}
    return [x for x in current if x.get("tariff_id") not in prev_ids]
