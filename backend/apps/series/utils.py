import requests
import json
from django.conf import settings

def get_currency_value(currency, init_date, end_date):
    currencies = {
        "UDI": "SP68257",
        "USD": "SF43718",
        "TIIE": "SF331451,SF43783,SF43878"
    }
    if currency in currencies.keys():
        currency_value = currencies[currency]
        url = f"https://www.banxico.org.mx/SieAPIRest/service/v1/series/{currency_value}/datos/{init_date}/{end_date}"
        request = requests.get(url=url,
                               headers={"content-type":"application/json", 'Bmx-Token': settings.BANXICO_TOKEN})
        return json.loads(request.text)
    else:
        return False

def calculate_currency_data(data):
    data_currency = data['bmx']['series'][0]['datos']
    values = [float(v['dato']) for v in data_currency]
    promedio = sum(values)/len(values)
    return (data_currency, promedio, max(values), min(values))
