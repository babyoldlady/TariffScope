from fastapi import APIRouter

router = APIRouter()

@router.get("/{issuer}/tariffs")
def operator_index(issuer: str):
    return {"issuer": issuer, "tariffs": []}
  
