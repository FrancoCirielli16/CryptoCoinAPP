from pydantic import BaseModel


class Crypto(BaseModel):
    id:int
    name: str
    symbol: str
    price: float
    volume_24h:float