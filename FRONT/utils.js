function getAuthenticatedUser() {
    var token = localStorage.getItem('token');
    var usuario_id = localStorage.getItem('usuario_id');
    return { token, usuario_id };
}