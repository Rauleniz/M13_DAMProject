document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevenir el envío del formulario por defecto

    var formData = new FormData(this); // Obtener los datos del formulario
    var username = formData.get("username");
    var password = formData.get("password");

    // enviar datos al backend para verificar las credenciales
    fetch("http://localhost:5000/login", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Si la respuesta es exitosa, devolver los datos JSON
        } else {
            throw new Error("Credenciales incorrectas"); // Si hay un error en la respuesta, lanzar un error
        }
    })
    .then(data => {
        // datos devueltos por el backend (token JWT)
        console.log("Token JWT:", data.token);
        // Redirigir al usuario a la página, mostrar un mensaje de éxito, etc.
        window.location.href = "miperfil.html"; //va a home_user.html una ves edite el menú del perfil
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
