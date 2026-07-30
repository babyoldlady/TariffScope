import os
import requests


FERC_API_BASE_URL = os.getenv("FERC_API_BASE_URL", "https://data.ferc.gov")
FERC_API_KEY = os.getenv("FERC_API_KEY", "")
FERC_TARIFF_ENDPOINT = os.getenv("FERC_TARIFF_ENDPOINT", "/api/tariffs")


def fetch_ferc_tariffs():
    headers = {}
    if FERC_API_KEY:
        headers["Authorization"] = f"Bearer {FERC_API_KEY}"

    url = f"{FERC_API_BASE_URL.rstrip('/')}{FERC_TARIFF_ENDPOINT}"
    response = requests.get(url, headers=headers, timeout=60)
    response.raise_for_status()

    payload = response.json()

    if isinstance(payload, list):
        return payload

    if isinstance(payload, dict):
        for key in ("data", "results", "items", "tariffs"):
            if key in payload and isinstance(payload[key], list):
                return payload[key]

    return []
