import secrets
from fastapi import APIRouter, Depends, HTTPException, Query, Request ,status
from fastapi.templating import Jinja2Templates
from db.client import db_client

router = APIRouter(
            tags=["VERIFY"],
            responses={status.HTTP_404_NOT_FOUND: {"Message": "No encontrado"}}
        )

templates = Jinja2Templates(directory="static/templates")

def check_token(token: str = Query(...)):
    # Verificar si el token existe en la base de datos
    verification_token = db_client.tokens.find_one({"token": token})
    if verification_token is None:
        raise HTTPException(status_code=404, detail="Token inválido")
    return verification_token["user_id"]


def generate_verification_link(user_id: str):
    # Generar un token único
    token = secrets.token_urlsafe(16)

    # Guardar el token de verificación asociado al usuario en la base de datos
    verification_token = {"user_id": user_id, "token": token}
    db_client.tokens.insert_one(verification_token)

    # Generar el enlace de verificación
    verification_link = f"https://cryptocontrol-1-k4873642.deta.app/verify/?token={token}"

    return verification_link


@router.get('/verify/')
async def verify_user(request: Request,token: str = Query(...), user_id: str = Depends(check_token)):
    
    result = db_client.users.find_one_and_update(
        {"_id": user_id},
        {"$set": {"disable": True}},
        return_document=True
    )
    if result is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return templates.TemplateResponse("index.html", {"request": request})
