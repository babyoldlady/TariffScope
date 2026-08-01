import os
import requests

FERC_API_BASE_URL = os.getenv("FERC_API_BASE_URL", "https://data.ferc.gov")


def fetch_data_assets():
    url = f"{FERC_API_BASE_URL.rstrip('/')}/data-assets/"
    response = requests.get(url, timeout=60)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    assets = fetch_data_assets()
    print(assets)
