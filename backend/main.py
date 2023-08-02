from fastapi import FastAPI
from fastapi.routing import APIRoute
from routers import crypto,users
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app = FastAPI(
    title="API CRYPTOS-COIN",
    description="Esta API proporciona funcionalidades para el registro y autenticación de usuarios, así como el manejo de peticiones relacionadas con criptomonedas. Permite realizar operaciones como el registro de nuevos usuarios, inicio de sesión, obtener detalles y valores de criptomonedas, y más. La API admite más de 1000 criptomonedas que existen en el mercado. Algunas de las operaciones de la API requieren autenticación mediante un token de acceso. Para obtener el token de acceso, los usuarios deben autenticarse utilizando su nombre de usuario y contraseña a través del endpoint de inicio de sesión. Una vez obtenido el token de acceso, debe ser incluido en el encabezado de autenticación (Authorization: Bearer <token>) en todas las solicitudes autenticadas subsiguientes.",
    version="1.0.0",
    tags=["ROOT"]
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(crypto.router)
app.include_router(users.router)

@app.get("/")
async def root():
    return "Hola FastAPI!"


# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C
# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc