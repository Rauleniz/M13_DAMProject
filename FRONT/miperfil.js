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
    .catch(async error => {
        try {
            throw error;
        } catch (error) {
            console.error('Error:', error);            
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
                tarjeta_nombre: nuevoNombre,
                tarjeta_apellido: nuevoApellido,
                tarjeta_email: nuevoEmail,
                tarjeta_estatus: nuevoEstatus,
                usertarjeta_usernamename: nuevoUsername, 
                tarjeta_password: nuevoPassword
            }),
            mode: 'cors'
        })
        .then(response => response.json())
        .then(data => {
            // Manejar la respuesta de la solicitud PUT
            console.log("Datos actualizados del usuario:", data);
            alert('Datos actualizados correctamente');
        })
        .catch(error => console.error('Error:', error));
    });

    // FACTURACION
    document.getElementById('guardar-btn').addEventListener('click', function() {
        var nuevoTitular = document.getElementById('tarjeta_titular').value;
        var nuevoNumeracion = document.getElementById('tarjeta_numeracion').value;
        var nuevoCaducidad = document.getElementById('tarjeta_fecha_caducidd').value;
        var nuevoCvc = document.getElementById('tarjeta_cvc').value;

        // Actualizar los datos del usuario
        fetch("http://127.0.0.1:5000/put/bancario/" + usuario_id , {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",                                   
                "Authorization": "Bearer " + token,
            },
            body: JSON.stringify({
                titular: nuevoTitular,
                numeracion: nuevoNumeracion,
                caducidad: nuevoCaducidad,
                cvc: nuevoCvc
            }),
            mode: 'cors'
        })
        .then(response => response.json())
        .then(data => {
            // Manejar la respuesta de la solicitud PUT
            console.log("Datos actualizados del usuario:", data);
            alert('Datos actualizados correctamente');
        })
        .catch(error => console.error('Error:', error));
    });


    // SERVICIO
    document.getElementById('guardar-btn').addEventListener('click', function() {
        var nuevoTecnico = document.getElementById('tarjeta_tecnico').value;
        var nuevoCheque = document.getElementById('tarjeta_cheque').value;
        var nuevoFinanciacion = document.getElementById('tarjeta_financiacion').value;
        var nuevoSeguro = document.getElementById('tarjeta_seguro').value;
        var nuevoFurgon = document.getElementById('tarjeta_furgon').value;

        // Actualizar los datos del usuario
        fetch("http://127.0.0.1:5000/put/servicio/" + usuario_id, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",                                   
                "Authorization": "Bearer " + token,
            },
            body: JSON.stringify({
                tarjeta_tecnico: nuevoTecnico,
                tarjeta_cheque: nuevoCheque,
                tarjeta_financiacion: nuevoFinanciacion,
                tarjeta_seguro: nuevoSeguro,
                tarjeta_furgon: nuevoFurgon
            }),
            mode: 'cors'
        })
        .then(response => response.json())
        .then(data => {
            console.log("Datos actualizados del servicio:", data);
            alert('Servicio actualizados correctamente');
            // event.target.reset();

        })
        .catch(error => console.error('Error:', error));
        alert('Error al dar de alta: ' + error.message);
    });
    


    // CAMBIAR DE PLAN

    document.getElementById('guardar-btn').addEventListener('click', function() {
        var nuevoPlan = document.getElementById('tarjeta_plan').value;

        // Actualizar los datos del usuario
        fetch("http://127.0.0.1:5000/put/plan/" + usuario_id, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",                                   
                "Authorization": "Bearer " + token,
            },
            body: JSON.stringify({
                tarjeta_plan: nuevoPlan,
            }),
            mode: 'cors'
        })
        .then(response => response.json())
        .then(data => {
            console.log("Datos actualizados del plan:", data);
            alert('Plan actualizado correctamente');
        })
        .catch(error => console.error('Error:', error));
    });

    // CANCELAR SUSCRIPCION
    document.getElementById('guardar-btn').addEventListener('click', function() {
        var nuevoCancelacion = document.getElementById('tarjeta_suscripcion').value;
      
        fetch("http://127.0.0.1:5000/delete/plan/" + usuario_id, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json",                                   
                "Authorization": "Bearer " + token,
            },
            body: JSON.stringify({
                tarjeta_suscripcion: nuevoCancelacion,
            }),
            mode: 'cors'
        })
        .then(response => response.json())
        .then(data => {
            console.log("Datos actualizados del servicio:", data);
            window.location.href = "cancelacion.html";
            // alert('Plan cancelado correctamente');
        })
        .catch(error => console.error('Error:', error));
    });




    
    //************************* */


    var datosActualizadosDiv = document.querySelector('.datos_actualizados');
    var datosFacturacionDiv = document.querySelector('.datos_facturacion');
    var datosServicioDiv = document.querySelector('.datos_servicio');
    var datosPlanDiv = document.querySelector('.datos_plan');
    var datosSuscripcionDiv = document.querySelector('.datos_suscripcion');

    // Oculta todos los divs al inicio
    datosActualizadosDiv.style.display = 'none';
    datosFacturacionDiv.style.display = 'none';
    datosServicioDiv.style.display = 'none';
    datosPlanDiv.style.display = 'none';
    datosSuscripcionDiv.style.display = 'none';
    document.querySelector(".edicion_perfil .guardar_cambios").style.display = "none";
    document.querySelector(".edicion_facturacion .guardar_cambios").style.display = "none";
    document.querySelector(".edicion_servicio .guardar_cambios").style.display = "none";
    document.querySelector(".edicion_plan .guardar_cambios").style.display = "none";
    document.querySelector(".edicion_suscripcion .guardar_cambios").style.display = "none";

    // Agrega event listeners a los botones
    document.getElementById('select-perfil-btn').addEventListener('click', function() {
        // Muestra el div de datos actualizados y oculta los demás
        datosActualizadosDiv.style.display = 'block';
        document.querySelector(".edicion_perfil .guardar_cambios").style.display = "block";
        datosFacturacionDiv.style.display = 'none';
        document.querySelector(".edicion_facturacion .guardar_cambios").style.display = "none";
        datosServicioDiv.style.display = 'none';
        document.querySelector(".edicion_servicio .guardar_cambios").style.display = "none";
        datosSuscripcionDiv.style.display = 'none';
        document.querySelector(".edicion_suscripcion .guardar_cambios").style.display = "none";
        datosPlanDiv.style.display = 'none';
        document.querySelector(".edicion_plan .guardar_cambios").style.display = "none";
        
    });

    document.getElementById('select-facturacion-btn').addEventListener('click', function() {
        // Muestra el div de datos de facturación y oculta los demás
        datosFacturacionDiv.style.display = 'block';
        document.querySelector(".edicion_facturacion .guardar_cambios").style.display = "block";
        datosActualizadosDiv.style.display = 'none';
        document.querySelector(".edicion_perfil .guardar_cambios").style.display = "none";
        datosServicioDiv.style.display = 'none';
        document.querySelector(".edicion_servicio .guardar_cambios").style.display = "none";
        datosPlanDiv.style.display = 'none';
        document.querySelector(".edicion_plan .guardar_cambios").style.display = "none";
        datosSuscripcionDiv.style.display = 'none';
        document.querySelector(".edicion_suscripcion .guardar_cambios").style.display = "none";
    });

    document.getElementById('select-servicio-btn').addEventListener('click', function() { 
        datosServicioDiv.style.display = 'block';
        document.querySelector(".edicion_servicio .guardar_cambios").style.display = "block";
        datosActualizadosDiv.style.display = 'none';
        document.querySelector(".edicion_perfil .guardar_cambios").style.display = "none";
        datosFacturacionDiv.style.display = 'none';
        document.querySelector(".edicion_facturacion .guardar_cambios").style.display = "none";
        datosSuscripcionDiv.style.display = 'none';
        document.querySelector(".edicion_suscripcion .guardar_cambios").style.display = "none";
        datosPlanDiv.style.display = 'none';
        document.querySelector(".edicion_plan .guardar_cambios").style.display = "none";
    });

    document.getElementById('select-plan-btn').addEventListener('click', function() { 
        datosPlanDiv.style.display = 'block';
        document.querySelector(".edicion_plan .guardar_cambios").style.display = "block";
        datosActualizadosDiv.style.display = 'none';
        document.querySelector(".edicion_perfil .guardar_cambios").style.display = "none";
        datosFacturacionDiv.style.display = 'none';
        document.querySelector(".edicion_facturacion .guardar_cambios").style.display = "none";
        datosServicioDiv.style.display = 'none';
        document.querySelector(".edicion_servicio .guardar_cambios").style.display = "none";
        datosSuscripcionDiv.style.display = 'none';
        document.querySelector(".edicion_suscripcion .guardar_cambios").style.display = "none";
    });

    document.getElementById('select-cancelar-btn').addEventListener('click', function() { 
        datosSuscripcionDiv.style.display = 'block';
        document.querySelector(".edicion_suscripcion .guardar_cambios").style.display = "block";
        datosActualizadosDiv.style.display = 'none';
        document.querySelector(".edicion_perfil .guardar_cambios").style.display = "none";
        datosFacturacionDiv.style.display = 'none';
        document.querySelector(".edicion_facturacion .guardar_cambios").style.display = "none";
        datosServicioDiv.style.display = 'none';
        document.querySelector(".edicion_servicio .guardar_cambios").style.display = "none";
        datosPlanDiv.style.display = 'none';
        document.querySelector(".edicion_plan .guardar_cambios").style.display = "none";
    });

    
    
    




  
});