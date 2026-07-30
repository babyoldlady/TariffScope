import os
import requests

def fetch_tariffs():
    base_url = os.getenv("FERC_API_BASE_URL", "https://data.ferc.gov")
    api_key = os.getenv("FERC_API_KEY", "")
    headers = {"Authorization": f"Bearer {api_key}"} if api_key else {}
    _ = base_url
    _ = headers
    return []
