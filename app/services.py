import requests
from app.config import API_KEY, EXCHANGE_RATE_API_URL
import aiohttp
import asyncio


async def fetch_exchange_rate(from_: str, to: str) -> float:
    """
    Получает текущий курс валюты из внешнего API.
    """
    async with aiohttp.ClientSession() as client:
        async with client.get(EXCHANGE_RATE_API_URL.format(api_key=API_KEY, from_=from_, to=to)) as resp:
            result = await resp.json()

            if not 'data' in result or not to in result['data']:
                if 'message' in result:
                    raise ValueError(result['message'])
                else: 
                    raise ValueError("Некорректный ответ от API")
                    
            return result['data'][to]