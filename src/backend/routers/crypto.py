from concurrent.futures import ThreadPoolExecutor
from fastapi import APIRouter, Request, Response, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests
from CoinAPI import crypto,data
from db.models.crypto import Crypto
from db.client import db_client

router = APIRouter(tags=["CRYPTOS"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})

def get_additional_info_from_db(name):
    
    # Realiza la búsqueda en la base de datos
    query = {"name": name}
    result = db_client.Icons.find_one(query)

    if result:
        return result["image"]
    else:
        return ""



def obtenerCryptos():
    cryptos = data()  # cryptos ya es una lista de objetos Future
    cryptos_set = set()  # Usamos un conjunto para mantener un registro de las criptomonedas únicas
    cryptos_list = []
    cached_info = {}  # Caché local para almacenar información adicional

    def process_crypto(data):
        name = data["name"]
        if name in cached_info:
            img = cached_info[name]
        else:
            img = get_additional_info_from_db(name)
            cached_info[name] = img

        if img and name not in cryptos_set:  # Verificamos si la criptomoneda ya está en el conjunto
            cryptos_set.add(name)  # Agregamos el nombre al conjunto de criptomonedas
            cryptos_list.append(Crypto(id=data["id"], name=data["name"], symbol=data["symbol"],
                                price=data["quote"]["USD"]["price"], volume_24h=data["quote"]["USD"]["volume_24h"],porcentaje=data["quote"]["USD"]["percent_change_1h"] ,image=img, market_cap=data["quote"]["USD"]["market_cap":]))
            print(data["name"])
    
    with ThreadPoolExecutor(max_workers=5) as executor:
        batch_size = 1000  # Puedes ajustar el tamaño del lote según tus necesidades
        # Itera sobre los objetos Future en cryptos y obtiene los resultados
        for future in cryptos:
            crypto_data = future.result()["data"]
            batches = [crypto_data[i:i + batch_size] for i in range(0, len(crypto_data), batch_size)]
            
            for batch in batches:
                futures = [executor.submit(process_crypto, data) for data in batch]
                for future in futures:
                    future.result()
            
    return cryptos_list






# OPERACIONES GET
@router.get("/cryptos")
async def cryptos():
    return crypto()
    dic = [{
        "name": "Bitcoin",
        "symbol": "ETH",
        "price": 50000,
        "market_cap": 1000000000,
        "porcentaje_1h":10000,
        "porcentaje_24h":1200,
        "volume_24h":21312
        # Agregar más detalles aquí
        },
        {
        "name": "Bitcoin",
        "symbol": "BTC",
        "price": 50000,
        "market_cap": 1000000000,
        "porcentaje_1h":10000,
        "porcentaje_24h":1200,
        "volume_24h":21312
        # Agregar más detalles aquí
        },
        {
        "name": "Bitcoin",
        "symbol": "BTC",
        "price": 50000,
        "market_cap": 1000000000,
        "porcentaje_1h":10000,
        "porcentaje_24h":1200,
        "volume_24h":21312
        # Agregar más detalles aquí
        },
        {
        "name": "Bitcoin",
        "symbol": "BTC",
        "price": 50000,
        "market_cap": 1000000000,
        "porcentaje_1h":10000,
        "porcentaje_24h":1200,
        "volume_24h":21312
        # Agregar más detalles aquí
        },{
        "name": "Bitcoin",
        "symbol": "BTC",
        "price": 50000,
        "market_cap": 1000000000,
        "porcentaje_1h":10000,
        "porcentaje_24h":1200,
        "volume_24h":21312
        # Agregar más detalles aquí
        },{
        "name": "Bitcoin",
        "symbol": "BTC",
        "price": 50000,
        "market_cap": 1000000000,
        "porcentaje_1h":10000,
        "porcentaje_24h":1200,
        "volume_24h":21312
        # Agregar más detalles aquí
        },
        {
        "name": "Bitcoin",
        "symbol": "BTC",
        "price": 50000,
        "market_cap": 1000000000,
        "porcentaje_1h":10000,
        "porcentaje_24h":1200,
        "volume_24h":21312
        # Agregar más detalles aquí
        },
        {
        "name": "Bitcoin",
        "symbol": "BTC",
        "price": 50000,
        "market_cap": 1000000000,
        "porcentaje_1h":10000,
        "porcentaje_24h":1200,
        "volume_24h":21312
        # Agregar más detalles aquí
        },
        {
        "name": "Bitcoin",
        "symbol": "BTC",
        "price": 50000,
        "market_cap": 1000000000,
        "porcentaje_1h":10000,
        "porcentaje_24h":1200,
        "volume_24h":21312
        # Agregar más detalles aquí
        },{
        "name": "Bitcoin",
        "symbol": "BTC",
        "price": 50000,
        "market_cap": 1000000000,
        "porcentaje_1h":10000,
        "porcentaje_24h":1200,
        "volume_24h":21312
        # Agregar más detalles aquí
        }
    ]
    return dic


@router.get("/crypto/{symbol}")
async def cryptos(symbol: str):
    crypto_details_data = {
    "BTC": {
        "name": "Bitcoin",
        "symbol": "BTC",
        "price": 50000,
        "market_cap": 1000000000,
        # Agregar más detalles aquí
        }
    }
    return crypto_details_data




