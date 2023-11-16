from concurrent.futures import ThreadPoolExecutor
from requests import Request, Session
import requests
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
from urllib3 import Retry
from db.models.crypto import Crypto
from keys import COIN_API_TEST, COIN_API
from requests.adapters import HTTPAdapter


def get_crypto(url, params, headers):

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=params, headers=headers)
        data = json.loads(response.text)
        return data
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return None


def data():
    session = Session()
    retries = Retry(total=5, backoff_factor=0.2,
                    status_forcelist=[500, 502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))

    url = COIN_API
    params = {
        'start': '1',
        'limit': '2500',
        'convert': 'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '16d3ed91-1857-492a-9903-ce8be1c08596',
        'Accept-Encoding': 'gzip',  # Habilitar compresión Gzip
    }
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = [executor.submit(get_crypto, url, params, headers)
                   for _ in range(5)]
    return results

def crypto():
    
    session = Session()
    cryptos_list = []

    try:
        response = session.get("https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=250&page=1&sparkline=false&price_change_percentage=1h%2C%2024h%2C%207d%2C%201y&locale=en")
        cryptos = json.loads(response.text)
        print(cryptos)
        for data in cryptos:
            if data["price_change_percentage_24h"] and data["price_change_percentage_1h_in_currency"]:
                cryptos_list.append(Crypto(id=data["id"], name=data["name"], symbol=data["symbol"],
                                    price=data["current_price"],price_change_24h=data["price_change_24h"], volume_24h=data["total_volume"],porcentaje_24h=data["price_change_percentage_24h"],porcentaje_1h=data["price_change_percentage_1h_in_currency"] ,image=data["image"], market_cap=data["market_cap"]))
        print(cryptos_list)
        return cryptos_list
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
        return None


if __name__ == "__main__":
    crypto()
