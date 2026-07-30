from backend.api.db import SessionLocal, engine
from backend.api.models import Base, TariffRecord
from backend.ingestion.ferc_client import fetch_ferc_tariffs
from backend.ingestion.normalize import normalize_tariff


def init_db():
    Base.metadata.create_all(bind=engine)


def ingest_tariffs(session, rows):
    count = 0
    for row in rows:
        item = normalize_tariff(row)

        existing = session.query(TariffRecord).filter_by(tariff_id=item["tariff_id"]).first()
        if existing:
            for key, value in item.items():
                setattr(existing, key, value)
        else:
            session.add(TariffRecord(**item))

        count += 1

    session.commit()
    return count


def main():
    init_db()
    rows = fetch_ferc_tariffs()
    with SessionLocal() as session:
        loaded = ingest_tariffs(session, rows)
    print(f"Ingested {loaded} tariff records")


if __name__ == "__main__":
    main()
