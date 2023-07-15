from typing import Any
import bcrypt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from db.models.user import AdditionalUserDataForm   
from db.models.user import User
from db.client import db_client
from db.schemas.user import user_schema, users_schema
from bson import ObjectId

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 10
SECRET = "201d573bd7d1344d3a3bfce1550b69102fd11be3db6d379508b6cccc58ea230b"

router = APIRouter(
    tags=["USERS"],
    responses={status.HTTP_404_NOT_FOUND: {"Message": "No encontrado"}}
)

oauth2 = OAuth2PasswordBearer(tokenUrl="/userdb/login")

crypt = CryptContext(schemes=["bcrypt"])

def search_user(field: str, key) -> User:
    """
    Busca un usuario por un campo específico en la base de datos.

    Args:
        field (str): Campo por el cual se realizará la búsqueda.
        key: Valor del campo por el cual se realizará la búsqueda.

    Returns:
        User: Objeto de tipo User que representa al usuario encontrado.
    """
    try:
        user = db_client.users.find_one({field: key})
        return User(**user_schema(user))
    except:
        return {"error": "No se encontró el usuario"}

def search_user_dic(filter: dict[str, Any]) -> User:
    """
    Busca un usuario en la base de datos utilizando un filtro específico.

    Args:
        filter (dict[str, Any]): Filtro para buscar el usuario en la base de datos.

    Returns:
        User: Objeto de tipo User que representa al usuario encontrado.
    """
    try:
        user = db_client.users.find_one(filter)
        return User(**user_schema(user))
    except:
        return {"error": "No se encontró el usuario"}

async def auth_user(token: str = Depends(oauth2)) -> User:
    """
    Verifica y autentica al usuario utilizando el token de acceso.

    Args:
        token (str): Token de acceso del usuario.

    Returns:
        User: Objeto de tipo User que representa al usuario autenticado.
    """
    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales de autenticación inválidas",
        headers={"WWW-Authenticate": "Bearer"}
    )
    try:
        user_id = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        print(user_id)
        if user_id is None:
            raise exception
    except JWTError:
        raise exception

    return search_user("_id", ObjectId(user_id))


async def current_user(user: User = Depends(auth_user)) -> User:
    """
    Obtiene el usuario actual autenticado.

    Args:
        user (User): Usuario autenticado.

    Returns:
        User: Usuario autenticado.
    """
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario inactivo"
        )
    return user

# OPERACIONES GET

@router.get("/userdb", response_model=list[User])
async def users() -> list[User]:
    """
    Obtiene la lista de todos los usuarios.

    Returns:
        list[User]: Lista de objetos User que representa a los usuarios.
    """
    return users_schema(db_client.users.find())

@router.get("/userdb/token")
async def user(user: User = Depends(current_user)) -> User:
    """
    Obtiene el usuario actual autenticado.

    Args:
        user (User): Usuario autenticado.

    Returns:
        User: Usuario autenticado.
    """
    return user

# POST

# LOGEAR UN USUARIO

@router.post("/userdb/login", status_code=status.HTTP_201_CREATED)
async def user(form: OAuth2PasswordRequestForm = Depends()) -> dict[str, str]:
    """
    Autentica a un usuario y devuelve un token de acceso.

    Args:
        form (OAuth2PasswordRequestForm): Formulario de solicitud de contraseña OAuth2.

    Returns:
        dict[str, str]: Diccionario que contiene el token de acceso y el tipo de token.
    """
    user_db = db_client.users.find_one({"username": form.username})
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto"
        )

    password_correct = bcrypt.checkpw(form.password.encode('utf-8'), user_db['password'])

    if not password_correct:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="La contraseña no es correcta"
        )

    access_token = {
        "sub": str(user_db["_id"]),
        "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }

    return {
        "access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM),
        "token_type": "bearer"
    }

# REGISTRAR USUARIO

@router.post("/userdb/register", status_code=status.HTTP_201_CREATED)
async def user(form: OAuth2PasswordRequestForm = Depends(), additional_data: AdditionalUserDataForm = Depends()) -> User:
    """
    Registra un nuevo usuario en la base de datos.

    Args:
        form (OAuth2PasswordRequestForm): Formulario de solicitud de contraseña OAuth2.
        additional_data (AdditionalUserDataForm): Formulario de datos adicionales del usuario.

    Returns:
        User: Objeto de tipo User que representa al usuario registrado.
    """
    if type(search_user_dic({"email": additional_data.email})) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="El usuario ya existe"
        )

    user_dict = dict(**form.__dict__, **additional_data.__dict__)
    user_dict["password"] = bcrypt.hashpw(form.password.encode('utf-8'), bcrypt.gensalt())
    id = db_client.users.insert_one(user_dict).inserted_id
  
    new_user = user_schema(db_client.users.find_one({"_id": id}))
    
    return new_user

# DELETE

@router.delete("/userdb", status_code=status.HTTP_204_NO_CONTENT)
async def user(form: OAuth2PasswordRequestForm = Depends()):
    """
    Elimina un usuario de la base de datos.

    Args:
        form (OAuth2PasswordRequestForm): Formulario de solicitud de contraseña OAuth2.

    Returns:
        dict[str, str]: Diccionario de respuesta con el mensaje de éxito o error.
    """
    user = search_user_dic({"username": form.username, "password": form.password})
    found = db_client.users.find_one_and_delete({"_id": ObjectId(user.id)})
    if not found:
        return {"error": "No se ha eliminado el usuario"}
