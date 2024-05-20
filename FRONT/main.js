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
});
