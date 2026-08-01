from __future__ import annotations

from backend.api.db import SessionLocal, engine
from backend.api.models import Base, TariffParty, Filing, Attachment, FilingRecord
from backend.ingestion.parse_etariff_xml import parse_etariff_xml


def init_db():
    Base.metadata.create_all(bind=engine)


def upsert_party(session, party_data):
    if not party_data or not party_data.get("company_id"):
        return None

    existing = (
        session.query(TariffParty)
        .filter_by(company_id=party_data["company_id"])
        .first()
    )

    if existing:
        for key, value in party_data.items():
            setattr(existing, key, value)
        return existing

    party = TariffParty(**party_data)
    session.add(party)
    return party


def upsert_filing(session, filing_data):
    if not filing_data or not filing_data.get("filing_id"):
        return None

    existing = (
        session.query(Filing)
        .filter_by(filing_id=filing_data["filing_id"])
        .first()
    )

    if existing:
        for key, value in filing_data.items():
            setattr(existing, key, value)
        return existing

    filing = Filing(**filing_data)
    session.add(filing)
    return filing


def add_attachments(session, filing_id, attachments):
    for item in attachments:
        session.add(
            Attachment(
                filing_id=filing_id,
                att_ref_code=item.get("att_ref_code"),
                att_desc=item.get("att_desc"),
                att_waiver_request=item.get("att_waiver_request"),
                att_filename=item.get("att_filename"),
                att_content_type_code=item.get("att_content_type_code"),
                att_security_level=item.get("att_security_level"),
                att_binary_data=item.get("att_binary_data"),
                source_system=item.get("source_system"),
            )
        )


def add_records(session, filing_id, records):
    for item in records:
        session.add(
            FilingRecord(
                filing_id=filing_id,
                record_id=item.get("record_id"),
                option_code=item.get("option_code"),
                record_title=item.get("record_title"),
                record_content_desc=item.get("record_content_desc"),
                record_version_num=item.get("record_version_num"),
                record_narrative_name=item.get("record_narrative_name"),
                collation_value=item.get("collation_value"),
                record_parent_id=item.get("record_parent_id"),
                proposed_effective_date=item.get("proposed_effective_date"),
                priority_order=item.get("priority_order"),
                record_content_type_code=item.get("record_content_type_code"),
                record_binary_data=item.get("record_binary_data"),
                record_plain_text=item.get("record_plain_text"),
                record_change_type=item.get("record_change_type"),
                associated_filing_id=item.get("associated_filing_id"),
                associated_record_id=item.get("associated_record_id"),
                associated_option_code=item.get("associated_option_code"),
                source_system=item.get("source_system"),
            )
        )


def load_xml_file(xml_path: str):
    init_db()
    parsed = parse_etariff_xml(xml_path)

    with SessionLocal() as session:
        party = upsert_party(session, parsed.get("party"))
        filing = upsert_filing(session, parsed.get("filing"))

        if filing:
            add_attachments(session, filing.filing_id, parsed.get("attachments", []))
            add_records(session, filing.filing_id, parsed.get("records", []))

        session.commit()

    return {
        "party_saved": bool(party),
        "filing_saved": bool(filing),
        "attachments_saved": len(parsed.get("attachments", [])),
        "records_saved": len(parsed.get("records", [])),
    }


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        raise SystemExit("Usage: python -m backend.ingestion.load_filings path/to/sample_filing.xml")

    result = load_xml_file(sys.argv[1])
    print(result)
