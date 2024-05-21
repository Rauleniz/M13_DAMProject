document.addEventListener("DOMContentLoaded", function() {
    var token = localStorage.getItem('token');
    var usuario_id = localStorage.getItem('usuario_id');
    if (token && usuario_id) {
        // El usuario está autenticado, muestra el menú de usuario
        document.querySelector('.boton_login').style.display = 'none';
        document.querySelector('.menu_user').style.display = 'block';
    } else {
        // El usuario no está autenticado, muestra el botón de login
        document.querySelector('.boton_login').style.display = 'block';
        document.querySelector('.menu_user').style.display = 'none';
    }

    var cookieConsent = document.getElementById('cookie-consent');
    var acceptCookiesButton = document.getElementById('accept-cookies');

    // Comprobar si el usuario ya ha aceptado las cookies
    if (!localStorage.getItem('cookiesAccepted')) {
        cookieConsent.style.display = 'block';
    }

    acceptCookiesButton.addEventListener('click', function() {
        // Guardar la aceptación en localStorage
        localStorage.setItem('cookiesAccepted', 'true');
        // Ocultar el aviso de cookies
        cookieConsent.style.display = 'none';
    });
});
