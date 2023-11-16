from pydantic import BaseModel


class Crypto(BaseModel):
    id:str
    name: str
    symbol: str
    price: float
    volume_24h:float
    image:str
    porcentaje_24h:float
    porcentaje_1h:float
    market_cap:float
    price_change_24h:float