
from attr import dataclass
from fastapi import Form
from pydantic import BaseModel
from typing import Optional

@dataclass
class AdditionalUserDataForm:
    email: str = Form()
    disable:bool | None = None
    fullname:str = Form()

class User(BaseModel):
    id: Optional[str]
    fullname:str
    username: str
    email:str

class UserDB(User):
    password: str