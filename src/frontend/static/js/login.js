document.getElementById('loginForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Evitar el envío del formulario predeterminado

    var username = document.getElementsByName('username')[0].value;
    var password = document.getElementsByName('password')[0].value;

    // Construir el objeto de datos a enviar
    var data = {
        username: username,
        password: password
    };

    // Realizar la solicitud POST a tu API
    fetch('http://127.0.0.1:8000/userdb/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(function (response) {
            return response.json();
        })
        .then(function (result) {
            // Manejar la respuesta de la API
            console.log(result);
            // Aquí puedes realizar acciones adicionales, como mostrar un mensaje de éxito o redireccionar a otra página
        })
        .catch(function (error) {
            // Manejar errores de la solicitud
            console.error(error);
        });
});
