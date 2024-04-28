



// CAJA 2 - INFO ACTUAL
// Supongamos que 'data' es el JSON recibido del backend con la información del usuario
const informacionActualUsuario = data;

// Actualizar los elementos <p> con la información actual del usuario
document.getElementById("direccion").textContent = informacionActualUsuario.direccion;
document.getElementById("email").textContent = informacionActualUsuario.email;
document.getElementById("descripcion").textContent = informacionActualUsuario.descripcion;
// Actualiza los demás campos de la misma manera si es necesario




document.addEventListener("DOMContentLoaded", function() {
    // Obtener referencia a los botones
    var editNombreBtn = document.getElementById("edit-nombre-btn");
    var editFacturacionBtn = document.getElementById("edit-facturacion-btn");
    var cambiarContrasenaBtn = document.getElementById("cambiar-contrasena-btn");
    var cambiarPlanBtn = document.getElementById("cambiar-plan-btn");
    var cancelarSuscripcionBtn = document.getElementById("cancelar-suscripcion-btn");

    // Agregar eventos de click a cada botón
    editNombreBtn.addEventListener("click", function() {
        // Lógica para editar el nombre
        // Aquí puedes enviar puedes usar la función fetch() una solicitud al backend para actualizar el nombre
    });

    editFacturacionBtn.addEventListener("click", function() {
        // Lógica para editar datos de facturación
        // Aquí puedes enviar puedes usar la función fetch() una solicitud al backend para actualizar el nombre
    });

    cambiarContrasenaBtn.addEventListener("click", function() {
        // Lógica para cambiar la contraseña
        // Aquí puedes enviar puedes usar la función fetch() una solicitud al backend para actualizar el nombre
    });

    cambiarPlanBtn.addEventListener("click", function() {
        // Lógica para cambiar de plan
        // Aquí puedes enviar puedes usar la función fetch() una solicitud al backend para actualizar el nombre
    });

    cancelarSuscripcionBtn.addEventListener("click", function() {
        // Lógica para cancelar la suscripción
        // Aquí puedes enviar puedes usar la función fetch() una solicitud al backend para actualizar el nombre
    });
});
