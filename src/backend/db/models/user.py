from attr import dataclass
from fastapi import Form
from pydantic import BaseModel
from typing import Optional

@dataclass
class AdditionalUserDataForm:
    email: str = Form()
    disable: Optional[bool] = None
    fullname: str = Form()

class User(BaseModel):
    id: Optional[str]
    fullname: str
    username: str
    email: str
    subs: list

class UserDB(User):
    password: str
