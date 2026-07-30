import uuid


def normalize_bool(value):
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        return value.strip().lower() in {"1", "true", "yes", "y", "effective", "active"}
    return False


def normalize_tariff(row):
    return {
        "tariff_id": str(row.get("tariff_id") or row.get("id") or uuid.uuid4()),
        "issuer": row.get("issuer") or row.get("company") or row.get("operator"),
        "tariff_no": row.get("tariff_no") or row.get("tariffNumber") or row.get("tariff_number"),
        "tariff_type": row.get("tariff_type") or row.get("type") or row.get("tariffType"),
        "product_type": row.get("product_type") or row.get("product") or row.get("commodity"),
        "origin": row.get("origin") or row.get("from"),
        "destination": row.get("destination") or row.get("to"),
        "regulator": row.get("regulator") or row.get("jurisdiction"),
        "status": row.get("status") or row.get("tariff_status"),
        "effective_yes_no": normalize_bool(row.get("effective_yes_no") or row.get("effective") or row.get("is_effective")),
        "effective_date": row.get("effective_date") or row.get("effectiveDate"),
        "filed_date": row.get("filed_date") or row.get("filedDate"),
        "rate_text": row.get("rate_text") or row.get("rates") or row.get("rate"),
        "rules_text": row.get("rules_text") or row.get("rules") or row.get("regulations"),
        "tariff_index_text": row.get("tariff_index_text") or row.get("index") or row.get("tariffIndex"),
        "company_contact_name": row.get("company_contact_name") or row.get("contact_name"),
        "company_contact_email": row.get("company_contact_email") or row.get("contact_email"),
        "company_contact_phone": row.get("company_contact_phone") or row.get("contact_phone"),
        "source_url": row.get("source_url") or row.get("url"),
        "source_system": row.get("source_system") or "FERC API",
    }
