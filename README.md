# CryptoCoinApp

## Descripción
CryptoCoinApp es una aplicación que te permite registrarte, iniciar sesión y acceder a información en tiempo real sobre precios de criptomonedas. Además, brinda la funcionalidad de seguir tus criptomonedas favoritas para recibir notificaciones por correo electrónico cada vez que su valor suba o baje.

## Características Principales
- Registro de usuarios: Permite a los usuarios registrarse proporcionando información básica como correo electrónico, nombre de usuario y contraseña.
- Inicio de sesión: Los usuarios pueden autenticarse en la aplicación utilizando su nombre de usuario y contraseña.
- Visualización de precios en tiempo real: La aplicación muestra los precios actualizados de una amplia variedad de criptomonedas, proporcionando información como el valor actual, cambios porcentuales y gráficos de rendimiento.
- Seguimiento de criptomonedas: Los usuarios pueden seleccionar las criptomonedas que desean seguir y recibir notificaciones por correo electrónico cada vez que haya cambios significativos en su valor.
- Notificaciones por correo electrónico: Cuando el valor de las criptomonedas seguidas por el usuario sube o baja más allá de un umbral establecido, se envía una notificación por correo electrónico con detalles sobre el cambio.

## Tecnologías Utilizadas
- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- Base de datos: MongoDB
- Integración de API: CoinAPI

# API de Gestión de Usuarios y Cryptomonedas

Esta API proporciona funcionalidades para el registro y autenticación de usuarios, así como el manejo de peticiones relacionadas con criptomonedas. Permite realizar operaciones como el registro de nuevos usuarios, inicio de sesión, obtener detalles y valores de criptomonedas, y más. La API admite más de 1000 criptomonedas que existen en el mercado.

## Características Principales

- Registro de usuarios: Permite a los usuarios registrarse proporcionando información como correo electrónico, nombre completo, nombre de usuario y contraseña.
- Inicio de sesión: Los usuarios pueden autenticarse mediante su nombre de usuario y contraseña, y se les proporciona un token de acceso para realizar solicitudes autenticadas posteriormente.
- Gestión de usuarios: Proporciona funcionalidades para obtener información de usuarios, actualizar datos de perfil y eliminar usuarios existentes.
- Consulta de Criptomonedas: Permite realizar consultas sobre criptomonedas específicas, obteniendo detalles como nombre, símbolo, precio actual, capitalización de mercado, volumen de operaciones, etc.
- Soporte para más de 1000 criptomonedas: La API proporciona información actualizada sobre una amplia gama de criptomonedas, lo que permite a los usuarios acceder a datos precisos y relevantes.

## Documentación

La documentación completa de la API, incluyendo detalles sobre las rutas, parámetros y respuestas, está disponible en [X](COMMING). Puedes explorar la documentación interactiva para comprender mejor cómo utilizar cada endpoint y aprovechar al máximo las funcionalidades de la API.

## Requisitos de Autenticación

Algunas de las operaciones de la API requieren autenticación mediante un token de acceso. Para obtener el token de acceso, los usuarios deben autenticarse utilizando su nombre de usuario y contraseña a través del endpoint de inicio de sesión. Una vez obtenido el token de acceso, debe ser incluido en el encabezado de autenticación (`Authorization: Bearer <token>`) en todas las solicitudes autenticadas subsiguientes.

## Ejemplos de Uso

Aquí hay algunos ejemplos de cómo utilizar la API:

1. Registro de un nuevo usuario:


```python
"POST /api/userdb/register"
{
"email": "usuario@example.com",
"full_name": "Nombre Completo",
"username": "nombre_usuario",
"password": "contraseña_segura"
}
```

2. Inicio de sesión:

```python
"POST /api/userdb/login"
{
"username": "nombre_usuario",
"password": "contraseña_segura"
}
```

La respuesta incluirá un token de acceso que se puede utilizar para autenticar solicitudes posteriores.

3. Obtener detalles de una criptomoneda:

Reemplaza `{crypto_id}` con el identificador o símbolo de la criptomoneda que deseas consultar.

Estos son solo algunos ejemplos de cómo interactuar con la API. Te recomiendo explorar la documentación completa para obtener más detalles sobre todas las funcionalidades disponibles.
