
// SOLICITUD GET al backend para obtener la información del usuario
fetch('http://127.0.0.1:5000/usuario/info', {
    method: 'GET',
    headers: {
        "Content-Type": "application/json"
    }
})
.then(response => response.json())
.then(data => {
    // Actualizar el contenido de los elementos HTML con los datos del usuario
    document.getElementById('direccion').innerHTML = data.direccion;
    document.getElementById('email').innerHTML = data.email;
    document.getElementById('descripcion').innerHTML = data.descripcion;
    document.getElementById('link_rss').textContent = data.link_rss;
})
.catch(error => {
    console.error('Error al obtener la información del usuario:', error);
});




// BOTONES DE SELECCIÓN
var botonEditarNombre = document.querySelector('#select-nombre-btn');
var botonEditarFacturacion = document.querySelector('#select-facturacion-btn');
var botonCambiarContrasena = document.querySelector('#select-contrasena-btn');
var botonCambiarPlan = document.querySelector('#select-plan-btn');
var botonCancelarSuscripcion = document.querySelector('#select-cancelar-btn');

// Agregar event listeners para cada botón
botonEditarNombre.addEventListener('click', function() {
    // Mostrar el input para editar el nombre
    mostrarCampoEdicion('nombre');
});

botonEditarFacturacion.addEventListener('click', function() {
    // Mostrar el input para editar los datos de facturación
    mostrarCampoEdicion('facturacion');
});

botonCambiarContrasena.addEventListener('click', function() {
    // Mostrar el input para cambiar la contraseña
    mostrarCampoEdicion('contrasenya');
});

botonCambiarPlan.addEventListener('click', function() {
    // Mostrar el input para cambiar el plan
    mostrarCampoEdicion('plan');
});

botonCancelarSuscripcion.addEventListener('click', function() {
    // Mostrar el input para cancelar la suscripción
    mostrarCampoEdicion('cancelar');
});



// Función para mostrar el campo de edición correspondiente
function mostrarCampoEdicion(campo) {
    // Ocultar todos los campos de edición
    var camposEdicion = document.querySelectorAll('.datos_actualizados input');
    camposEdicion.forEach(function(input) {
        input.style.display = 'none';
    });

    // Mostrar el campo de edición correspondiente
    var campoEdicion = document.querySelector('#' + campo);
    campoEdicion.style.display = 'block';
}



// BOTÓN GUARDAR
var botonGuardar = document.querySelector('#guardar-btn');
botonGuardar.addEventListener('click', function() {
    // Obtener el valor del campo de edición activo
    var campoEdicionActivo = document.querySelector('.datos_actualizados input[style="display: block"]');
    var nuevoValor = campoEdicionActivo.value;

    // Enviar solicitud PATCH al backend con el nuevo valor
    var endpoint = 'http://localhost:5000/usuario/actualizar/' + campoEdicionActivo.id;
    var data = {};
    data[campoEdicionActivo.name] = nuevoValor;

    fetch(endpoint, {
        method: 'PATCH',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(function(response) {
        if (response.ok) {
            // Si la solicitud fue exitosa, mostrar un mensaje al usuario
            console.log('Datos actualizados correctamente');
        } else {
            // Si hubo un error en la solicitud, mostrar un mensaje de error
            console.error('Error al actualizar los datos:', response.statusText);
        }
    })
    .catch(function(error) {
        // Si hubo un error en la solicitud, mostrar un mensaje de error
        console.error('Error en la solicitud:', error);
    });
});



// CARGAR LA PÁGINA CON LA INFO ACTUAL DEL USUARIO
function actualizarInformacionUsuario() {
    fetch('/usuario/informacion', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            // Aquí puedes incluir el token de autenticación si es necesario
            // 'Authorization': 'Bearer ' + authToken
        }
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error al obtener la información del usuario');
        }
    })
    .then(data => {
        // Actualizar la sección de información actual en la página con los nuevos datos
        document.getElementById('direccion').textContent = data.direccion;
        document.getElementById('email').textContent = data.email;
        document.getElementById('descripcion').textContent = data.descripcion;
        // Actualizar otros campos según sea necesario

        // Opcional: Mostrar un mensaje de éxito o realizar otras acciones después de la actualización
        console.log('Información de usuario actualizada con éxito');
    })
    .catch(error => {
        console.error('Error:', error);
        // Manejar errores, mostrar mensajes de error, etc.
    });
}

// Llamar a la función para actualizar la información del usuario después de una actualización exitosa
actualizarInformacionUsuario();


