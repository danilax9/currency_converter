from fastapi import FastAPI, HTTPException, Query
from app.services import fetch_exchange_rate

app = FastAPI(title="Currency Converter API")

@app.get("/api/rates")
async def convert_currency(to: str, value: float, from_: str = Query(alias="from")):
    """
    Конвертирует валюту из одной в другую.
    Пример запроса: /api/rates?from=USD&to=RUB&value=1
    """
    try:
        rate = await fetch_exchange_rate(from_, to)
        return {"result": round(rate * value, 2)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))