//Obtener datos actuales del usuario
fetch('/usuario', {
    method: 'GET'
})
.then(response => response.json())
.then(usuario => {
    // Rellenar los campos del formulario con los datos actuales del usuario
    document.getElementById('nombre').value = usuario.nombre;
    document.getElementById('apellidos').value = usuario.apellidos;
    document.getElementById('email').value = usuario.email;
});

// Manejar el envío del formulario de actualización
document.getElementById('formulario-actualizacion').addEventListener('submit', function(event) {
    event.preventDefault();

    // Obtener los datos actualizados del formulario
    const nuevoEmail = document.getElementById('email').value;

    // Enviar los datos actualizados al backend
    fetch('/usuario', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ email: nuevoEmail })
    })
    .then(response => {
        if (response.ok) {
            alert('Correo electrónico actualizado correctamente');
            // Actualizar la página o redirigir a otra página si es necesario
        } else {
            alert('Hubo un error al actualizar el correo electrónico');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Hubo un error al actualizar el correo electrónico');
    });
});
