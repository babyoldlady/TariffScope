from backend.ingestion.ferc_client import fetch_tariffs
from backend.ingestion.normalize import normalize_tariff

def run():
    raw_rows = fetch_tariffs()
    normalized = [normalize_tariff(r) for r in raw_rows]
    return normalized

if __name__ == "__main__":
    data = run()
    print(f"Loaded {len(data)} tariff records")
