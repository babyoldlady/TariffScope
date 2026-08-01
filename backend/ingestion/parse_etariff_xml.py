from __future__ import annotations

from pathlib import Path
import base64
import xml.etree.ElementTree as ET


def _text(node, path: str, default=None):
    if node is None:
        return default
    found = node.find(path)
    if found is None or found.text is None:
        return default
    return found.text.strip()


def _int_text(value):
    if value is None or value == "":
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def parse_etariff_xml(xml_path: str | Path) -> dict:
    """
    Parse an eTariff XML filing into a dict with:
    - party
    - filing
    - attachments
    - records
    """
    xml_path = Path(xml_path)
    tree = ET.parse(xml_path)
    root = tree.getroot()

    ns = {"x": "http://ferc.gov/etariff.xsd"}

    filing_node = root.find(".//x:ferc_filing_data", ns)
    if filing_node is None:
        return {
            "party": None,
            "filing": None,
            "attachments": [],
            "records": [],
        }

    # Party / company info
    party = {
        "company_id": _text(filing_node, "x:company_id"),
        "lead_applicant_id": _text(filing_node, "x:lead_applicant_id"),
        "source_system": "eTariff XML",
    }

    # Filing header info
    filing = {
        "schema_version": _text(filing_node, "x:schema_version"),
        "company_id": _text(filing_node, "x:company_id"),
        "lead_applicant_id": _text(filing_node, "x:lead_applicant_id"),
        "tariff_id": _int_text(_text(filing_node, "x:tariff_id")),
        "tariff_title": _text(filing_node, "x:tariff_title"),
        "filing_id": _int_text(_text(filing_node, "x:filing_id")),
        "filing_title": _text(filing_node, "x:filing_title"),
        "filing_type": _int_text(_text(filing_node, "x:filing_type")),
        "associated_filing_id": _int_text(_text(filing_node, "x:associated_filing_id")),
        "validation_email": _text(filing_node, "x:validation_email"),
        "pay_confirm_code": _text(filing_node, "x:pay_confirm_code"),
        "suspend_motion": _text(filing_node, "x:suspend_motion"),
        "source_system": "eTariff XML",
        "source_url": None,
    }

    # Attachments
    attachments = []
    for att in filing_node.findall("x:attachment_data", ns):
        binary_text = _text(att, "x:att_binary_data")
        attachments.append(
            {
                "att_ref_code": _int_text(_text(att, "x:att_ref_code")),
                "att_desc": _text(att, "x:att_desc"),
                "att_waiver_request": _text(att, "x:att_waiver_request"),
                "att_filename": _text(att, "x:att_filename"),
                "att_content_type_code": _int_text(_text(att, "x:att_content_type_code")),
                "att_security_level": _text(att, "x:att_security_level"),
                "att_binary_data": binary_text,
                "source_system": "eTariff XML",
            }
        )

    # Records
    records = []
    for rec in filing_node.findall("x:record_data", ns):
        record_binary = _text(rec, "x:record_binary_data")
        if record_binary:
            try:
                base64.b64decode(record_binary, validate=False)
            except Exception:
                # If it's not valid base64, we still keep the raw string
                pass

        records.append(
            {
                "record_id": _int_text(_text(rec, "x:record_id")),
                "option_code": _text(rec, "x:option_code"),
                "record_title": _text(rec, "x:record_title"),
                "record_content_desc": _text(rec, "x:record_content_desc"),
                "record_version_num": _text(rec, "x:record_version_num"),
                "record_narrative_name": _text(rec, "x:record_narrative_name"),
                "collation_value": _int_text(_text(rec, "x:collation_value")),
                "record_parent_id": _int_text(_text(rec, "x:record_parent_id")),
                "proposed_effective_date": _text(rec, "x:proposed_effective_date"),
                "priority_order": _int_text(_text(rec, "x:priority_order")),
                "record_content_type_code": _int_text(_text(rec, "x:record_content_type_code")),
                "record_binary_data": record_binary,
                "record_plain_text": _text(rec, "x:record_plain_text"),
                "record_change_type": _text(rec, "x:record_change_type"),
                "associated_filing_id": _int_text(_text(rec, "x:associated_filing_id")),
                "associated_record_id": _int_text(_text(rec, "x:associated_record_id")),
                "associated_option_code": _text(rec, "x:associated_option_code"),
                "source_system": "eTariff XML",
            }
        )

    return {
        "party": party,
        "filing": filing,
        "attachments": attachments,
        "records": records,
    }
