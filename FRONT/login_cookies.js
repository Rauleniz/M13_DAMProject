document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevenir el envío del formulario por defecto

    var formData = new FormData(this); // Obtener los datos del formulario

    // enviar datos al backend para verificar las credenciales
    fetch("http://localhost:5000/logincookies", {
        method: "POST",
        body: formData // Enviar datos como formulario en lugar de JSON
    })
    .then(response => {
        if (response.ok) {
            // Manejar las cookies de la respuesta
            var cookies = response.headers.get('Set-Cookie');
            // Redirigir al usuario a la página, mostrar un mensaje de éxito, etc.
            window.location.href = "miperfil.html"; //va a home_user.html una ves edite el menú del perfil
        } else {
            throw new Error("Credenciales incorrectas"); // Si hay un error en la respuesta, lanzar un error
        }
    })
    .catch(error => {
        // info error en el proceso de inicio de sesión
        console.error("Error:", error.message);
        //mensaje de error en el formulario
        var errorMessage = document.createElement("p");
        errorMessage.textContent = "Credenciales incorrectas";
        this.appendChild(errorMessage);
    });
});
