document.addEventListener("DOMContentLoaded", function() {
    var token = localStorage.getItem('token');
    var usuario_id = localStorage.getItem('usuario_id');
    console.log(token)
    console.log(usuario_id)

    fetch("http://127.0.0.1:5000/get/ubicacion/" + usuario_id , {
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
            throw new Error("Error al obtener la información de la etiqueta");
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
        var nuevoLat = document.getElementById('tarjeta_lat').value;
        var nuevoLng = document.getElementById('tarjeta_lng').value;
        var nuevoDescripcion = document.getElementById('tarjeta_descripcion').value;
        var nuevoRedes1 = document.getElementById('tarjeta_redes1').value;
        var nuevoRedes2 = document.getElementById('tarjeta_redes2').value;
        var nuevoRedes3 = document.getElementById('tarjeta_redes3').value;
        var nuevoRedes4 = document.getElementById('tarjeta_redes4').value;


        // Actualizar los datos del usuario
        fetch("http://127.0.0.1:5000/post/ubicacion/" + usuario_id , {
            method: "POST",
            headers: {
                "Content-Type": "application/json",                                   
                "Authorization": "Bearer " + token,
            },
            body: JSON.stringify({
                lat: nuevoLat,
                lng: nuevoLng,
                descripcion: nuevoDescripcion,
                link1: nuevoRedes1,
                link2: nuevoRedes2,
                link3: nuevoRedes3,
                link4: nuevoRedes4,

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



    // IMG
    document.getElementById('guardar-btn').addEventListener('click', function() {
        var nuevoImg = document.getElementById('tarjeta_tecnico').value;

        fetch("http://127.0.0.1:5000/post/multimedia/" + usuario_id, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",                                   
                "Authorization": "Bearer " + token,
            },
            body: JSON.stringify({
                img: nuevoImg,
            }),
            mode: 'cors'
        })
        .then(response => response.json())
        .then(data => {
            console.log("Datos actualizados del servicio:", data);
        })
        .catch(error => console.error('Error:', error));
    });
    
    // CANCION
    document.getElementById('guardar-btn').addEventListener('click', function() {
        var nuevoSong = document.getElementById('tarjeta_tecnico').value;

        fetch("http://127.0.0.1:5000/post/multimedia/" + usuario_id, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",                                   
                "Authorization": "Bearer " + token,
            },
            body: JSON.stringify({
                song: nuevoSong,
            }),
            mode: 'cors'
        })
        .then(response => response.json())
        .then(data => {
            console.log("Datos actualizados del servicio:", data);
        })
        .catch(error => console.error('Error:', error));
    });




    
    //************************* */


    var datosEtiquetaDiv = document.querySelector('.datos_etiqueta');
    var datosImgDiv = document.querySelector('.datos_img');
    var datosSongDiv = document.querySelector('.datos_song');

    // Oculta todos los divs al inicio
    datosEtiquetaDiv.style.display = 'none';
    datosImgDiv.style.display = 'none';
    datosSongDiv.style.display = 'none';

    document.querySelector(".edicion_etiqueta .guardar_cambios").style.display = "none";
    document.querySelector(".edicion_img .guardar_cambios").style.display = "none";
    document.querySelector(".edicion_song .guardar_cambios").style.display = "none";

    // Agrega event listeners a los botones
    document.getElementById('select-etiqueta-btn').addEventListener('click', function() {
        datosEtiquetaDiv.style.display = 'block';
        document.querySelector(".edicion_etiqueta .guardar_cambios").style.display = "block";
        datosImgDiv.style.display = 'none';
        document.querySelector(".edicion_img .guardar_cambios").style.display = "none";
        datosSongDiv.style.display = 'none';
        document.querySelector(".edicion_song .guardar_cambios").style.display = "none";
        
    });

    document.getElementById('select-img-btn').addEventListener('click', function() {
        datosImgDiv.style.display = 'block';
        document.querySelector(".edicion_img .guardar_cambios").style.display = "block";
        datosEtiquetaDiv.style.display = 'none';
        document.querySelector(".edicion_etiqueta .guardar_cambios").style.display = "none";
        datosSongDiv.style.display = 'none';
        document.querySelector(".edicion_song .guardar_cambios").style.display = "none";
    });

    document.getElementById('select-song-btn').addEventListener('click', function() { 
        datosSongDiv.style.display = 'block';
        document.querySelector(".edicion_song .guardar_cambios").style.display = "block";
        datosEtiquetaDiv.style.display = 'none';
        document.querySelector(".edicion_etiqueta .guardar_cambios").style.display = "none";
        datosImgDiv.style.display = 'none';
        document.querySelector(".edicion_img .guardar_cambios").style.display = "none";
    });      

  
});