document.addEventListener("DOMContentLoaded", function() {
    var token = localStorage.getItem('token');
    var usuario_id = localStorage.getItem('usuario_id');
    console.log(token)
    console.log(usuario_id)

    fetch("http://127.0.0.1:5000/get/usuario/" + usuario_id , {
        method: "GET",
        headers: {
            "Content-Type": "application/json",                                   
            "Authorization": "Bearer " + token,
        },
        mode: 'cors'
    })
    .then(response => {
        if (response.ok) {
            return response.json(); // Si la respuesta es exitosa, devolver los datos JSON
        } else {
            throw new Error("Error al obtener la información del usuario");
        }
    })
    // .then(data => {
    //     // Manejar la respuesta aquí y actualizar la interfaz de usuario con la información del usuario
    //     console.log("Datos del usuario:", data);
    //     document.getElementById('nombre').textContent = data.nombre;
    //     document.getElementById('email').textContent = data.email;
    //     document.getElementById('descripcion').textContent = data.descripcion;
    //     document.getElementById('link_rrss1').textContent = data.link_rrss1;

    // })
    .catch(async error => {
        try {
            throw error;
        } catch (error) {
            console.error('Error:', error);
            // Manejar errores de obtener la información del usuario
        }
    });

    // Event listener para el botón de guardar
    document.getElementById('guardar-btn').addEventListener('click', function() {
        var nuevoNombre = document.getElementById('tarjeta_nombre').value;
        var nuevoApellido = document.getElementById('tarjeta_apellido').value;
        var nuevoEmail = document.getElementById('tarjeta_email').value;
        var nuevoEstatus = document.getElementById('tarjeta_estatus').value;
        var nuevoUsername = document.getElementById('tarjeta_username').value;
        var nuevoPassword = document.getElementById('tarjeta_password').value;

        // Actualizar los datos del usuario
        fetch("http://127.0.0.1:5000/patch/usuario/" + usuario_id , {
            method: "PATCH",
            headers: {
                "Content-Type": "application/json",                                   
                "Authorization": "Bearer " + token,
            },
            body: JSON.stringify({
                nombre: nuevoNombre,
                apellidos: nuevoApellido,
                email: nuevoEmail,
                estatus: nuevoEstatus,
                username: nuevoUsername, 
                password: nuevoPassword
            }),
            mode: 'cors'
        })
        .then(response => response.json())
        .then(data => {
            // Manejar la respuesta de la solicitud PUT
            console.log("Datos actualizados del usuario:", data);
        })
        .catch(error => console.error('Error:', error));
    });

    // Aquí puedes agregar más event listeners para otros botones, como el de añadir una red social

    
    //************************* */


    var datosActualizadosDiv = document.querySelector('.datos_actualizados');
    var datosFacturacionDiv = document.querySelector('.datos_facturacion');
    var datosContrasenyaDiv = document.querySelector('.datos_contrasenya');
    var datosPlanDiv = document.querySelector('.datos_plan');
    var datosSuscripcionDiv = document.querySelector('.datos_suscripcion');

    // Oculta todos los divs al inicio
    datosActualizadosDiv.style.display = 'none';
    datosFacturacionDiv.style.display = 'none';
    datosContrasenyaDiv.style.display = 'none';
    datosPlanDiv.style.display = 'none';
    datosSuscripcionDiv.style.display = 'none';
    document.querySelector(".edicion_perfil .guardar_cambios").style.display = "none";
    document.querySelector(".edicion_facturacion .guardar_cambios").style.display = "none";
    document.querySelector(".edicion_contrasenya .guardar_cambios").style.display = "none";
    document.querySelector(".edicion_plan .guardar_cambios").style.display = "none";
    document.querySelector(".edicion_suscripcion .guardar_cambios").style.display = "none";

    // Agrega event listeners a los botones
    document.getElementById('select-perfil-btn').addEventListener('click', function() {
        // Muestra el div de datos actualizados y oculta los demás
        datosActualizadosDiv.style.display = 'block';
        document.querySelector(".edicion_perfil .guardar_cambios").style.display = "block";
        datosFacturacionDiv.style.display = 'none';
        document.querySelector(".edicion_facturacion .guardar_cambios").style.display = "none";
        datosContrasenyaDiv.style.display = 'none';
        document.querySelector(".edicion_contrasenya .guardar_cambios").style.display = "none";
    });

    document.getElementById('select-facturacion-btn').addEventListener('click', function() {
        // Muestra el div de datos de facturación y oculta los demás
        datosFacturacionDiv.style.display = 'block';
        document.querySelector(".edicion_facturacion .guardar_cambios").style.display = "block";
        datosActualizadosDiv.style.display = 'none';
        document.querySelector(".edicion_perfil .guardar_cambios").style.display = "none";
        datosContrasenyaDiv.style.display = 'none';
        document.querySelector(".edicion_contrasenya .guardar_cambios").style.display = "none";
    });

    document.getElementById('select-contrasenya-btn').addEventListener('click', function() { 
        datosContrasenyaDiv.style.display = 'block';
        document.querySelector(".edicion_contrasenya .guardar_cambios").style.display = "block";
        datosActualizadosDiv.style.display = 'none';
        document.querySelector(".edicion_perfil .guardar_cambios").style.display = "none";
        datosFacturacionDiv.style.display = 'none';
        document.querySelector(".edicion_facturacion .guardar_cambios").style.display = "none";
    });

    
    
    




  
});