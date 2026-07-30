from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/")
def list_tariffs(
    issuer: str | None = Query(default=None),
    tariff_type: str | None = Query(default=None),
    origin: str | None = Query(default=None),
    destination: str | None = Query(default=None),
    product_type: str | None = Query(default=None),
    regulator: str | None = Query(default=None),
    status: str | None = Query(default=None),
):
    return {
        "filters": {
            "issuer": issuer,
            "tariff_type": tariff_type,
            "origin": origin,
            "destination": destination,
            "product_type": product_type,
            "regulator": regulator,
            "status": status,
        },
        "results": []
    }

@router.get("/{tariff_id}")
def get_tariff(tariff_id: str):
    return {"tariff_id": tariff_id}
