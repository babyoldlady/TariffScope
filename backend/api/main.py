from fastapi import FastAPI
from backend.api.routers import tariffs, operators, subscriptions

app = FastAPI(title="TariffScope API", version="0.1.0")

app.include_router(tariffs.router, prefix="/tariffs", tags=["tariffs"])
app.include_router(operators.router, prefix="/operators", tags=["operators"])
app.include_router(subscriptions.router, prefix="/subscriptions", tags=["subscriptions"])

@app.get("/health")
def health():
    return {"status": "ok"}
