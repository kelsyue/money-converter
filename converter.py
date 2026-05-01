import os
import requests
from dotenv import load_dotenv

load_dotenv() 

def convert_currency(amount, from_currency, to_currency):
    api_key = os.getenv("EXCHANGE_RATE_API_KEY")

    if from_currency.upper() == to_currency.upper():
        return float(amount)

    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency.upper()}"

    try:
        response = requests.get(url)
        data = response.json()

        if data["result"] == "success":
            rates = data["conversion_rates"]
            rate = rates.get(to_currency.upper())

            return float(amount * rate) if rate else None

    except Exception as e:
        print(f"Error: {e}")
        return None