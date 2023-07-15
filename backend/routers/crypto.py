from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from CoinAPI import get_cryptos
from db.models.crypto import Crypto

router = APIRouter(tags=["CRYPTOS"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "No encontrado"}})



def obtenerCryptos():
    cryptos = get_cryptos()
    cryptos_list = []
    for c in cryptos["data"]:
        cryptos_list.append(Crypto(id = c["id"], name = c["name"] ,symbol = c["symbol"] ,price = c["quote"]["USD"]["price"] ,volume_24h = c["quote"]["USD"]["volume_24h"]))
    return cryptos_list


#OPERACIONES GET


@router.get("/cryptos")
async def cryptos():
    return obtenerCryptos()

@router.get("/cryptos/{symbol}")
async def cryptos(symbol:str):
    cryptos = obtenerCryptos()
    for c in cryptos:
        if (c.symbol == symbol):
            return c
    return {"message": "No encontrado"}

