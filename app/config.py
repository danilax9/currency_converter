from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY не найден в окружении!")

EXCHANGE_RATE_API_URL = (
    "https://api.freecurrencyapi.com/v1/latest"
    "?apikey={api_key}&base_currency={from_}&currencies={to}"
)