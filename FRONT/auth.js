document.addEventListener('DOMContentLoaded', function() {
    var token = localStorage.getItem('token');
    var usuario_id = localStorage.getItem('usuario_id');
    console.log(token)
    console.log(usuario_id)

    const isLoggedIn = localStorage.getItem('loggedIn') === 'true';
    document.querySelectorAll('.menu-general').forEach(el => {
        el.style.display = isLoggedIn ? 'none' : 'block';
    });
    document.querySelectorAll('.menu-usuario').forEach(el => {
        el.style.display = isLoggedIn ? 'block' : 'none';
    });

    document.getElementById('logout').addEventListener('click', function() {
        localStorage.setItem('loggedIn', 'false');
        localStorage.removeItem('token');
        localStorage.removeItem('usuario_id');
        window.location.href = 'index.html';
    });
});

// Función de inicio de sesión para pruebas
function login() {
    localStorage.setItem('loggedIn', 'true');
    localStorage.setItem('token', 'your-token-here'); 
    localStorage.setItem('usuario_id', 'your-user-id-here'); 
    window.location.href = 'miperfil.html';
}
