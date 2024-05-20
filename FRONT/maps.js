document.addEventListener("DOMContentLoaded", function() {
    var token = localStorage.getItem('token');
    var usuario_id = localStorage.getItem('usuario_id');
    console.log(token)
    console.log(usuario_id)


    // inicializar mapa (Barcelona centro. Zoom de 13)
    var map = L.map('map').setView([41.3868115, 2.172877], 13);

    // Añadir capa de OpenStreetMap y créditos
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    }).addTo(map);

    // Control de escala
    L.control.scale().addTo(map);

    //icono 
    var iconMap = L.icon({
        iconUrl: 'img/icon.png',

        iconSize:     [64, 64], 
        iconAnchor:   [22, 94], 
        popupAnchor:  [-3, -76] 
    });

    //A - añadir marcador individual (la etiqueta) individual
    // var marker = L.marker([41.39, 2.17],{icon: iconMap}).addTo(map);
    // marker.bindPopup("Raúl\nEtiqueta Demo\nArtista").openPopup();


    //B - array de marcadores (se añaden varios marcadores)
    // Array de objetos, cada uno representa un marcador
    var markers = [
        {latlng: [41.3868115, 2.172877], text: "Raúl\nStoner electrónica\nArtista"},
        {latlng: [41.3837, 2.16534], text: "The Band\nSomos una banda de rock\nArtista"},
        {latlng: [41.38986, 2.16482], text: "Rumba Sónica\nRumba tradicional\nArtista"}
    ];

    for (var i = 0; i < markers.length; i++) {
        // Crear un marcador para cada objeto en el array
        var marker = L.marker(markers[i].latlng, {icon: iconMap}).addTo(map);
        // Añadir un popup al marcador
        marker.bindPopup(markers[i].text).openPopup();
    }

    // B - etiqueta para conocer las coordenas
    var popup = L.popup()
    .setLatLng([41.3868115, 2.172877])
    .setContent("Selecciona cualquier icono")
    .openOn(map);


    // ---- Función para etiqueta individual
    // function onMapClick(e) {
    //     popup
    //         .setLatLng(e.latlng)
    //         .setContent(e.latlng.toString())
    //         .openOn(map);
    // }


    // map.on('click', onMapClick);


    // En el SetContent los usuarios logados pueden crear la ubicación de la etiqueta
    if (token && usuario_id) {
        map.on('click', function(e) {
            var popup = L.popup()
                .setLatLng(e.latlng)
                .setContent('<input type="text" id="descripcion" placeholder="Descríbete!"><br>' +
                            '<input type="text" id="link1" placeholder="Pon el link da tus redes"><br>' +
                            '<input type="text" id="link2" placeholder="Pon el link da tus redes"><br>' +
                            '<input type="text" id="link3" placeholder="Pon el link da tus redes"><br>' +
                            '<input type="text" id="link4" placeholder="Pon el link da tus redes"><br>' +
                            '<input type="file" id="audioFile" accept="audio/*">' +
                            '<button onclick="saveMarker()">Guardar</button>' + e.latlng.toString())
                .openOn(map);
        });
    }


    // GUARDAR LA NUEVA ETIQUETA EN EL BACKEND

    function saveMarker() {
        var descripcion = document.getElementById('descripcion').value;
        var link1 = document.getElementById('link1').value;
        var link2 = document.getElementById('link2').value;
        var link3 = document.getElementById('link3').value;
        var link4 = document.getElementById('link4').value;
        var audioFile = document.getElementById('audioFile').files[0];
        var latlng = popup.getLatLng();
        var lat = latlng.lat;
        var lng = latlng.lng;

        // Crear el objeto con los datos del marcador
        var newMarker = {latlng: [lat, lng], text: descripcion + '\n' + link1 + '\n' + link2 + '\n' + link3 + '\n' + link4};

            // ***** Crear el objeto FormData y añadir los datos junto con el archivo de Audio
            // var formData = new FormData();
            // formData.append('audioFile', audioFile);
            // formData.append('lat', lat);
            // formData.append('lng', lng);

        // Añadir el nuevo marcador al array de marcadores
        markers.push(newMarker);

        // Crear el objeto con los datos del marcador para enviar al servidor
        var data = {lat: lat, lng: lng, descripcion: descripcion, link1: link1, link2: link2, link3: link3, link4: link4};

        // Enviar la petición POST al servidor
        fetch('http://127.0.0.1:5000/post/ubicacion' + usuario_id, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
                "Authorization": "Bearer " + token,
            },
            body: JSON.stringify(data),
            // ***** Con archivo de audio no puede enviarse un json, ha de ser un FormData:
            //body: formData,
        })
        .then(response => response.json())
        .then(data => {
            console.log('Marcador guardado con éxito:', data);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }


    // Supongamos que 'markers' es un array de objetos, donde cada objeto tiene las propiedades 'latlng' y 'text'
    // var markers = /* Aquí iría la respuesta del servidor */"";

    // for (var i = 0; i < markers.length; i++) {
    //     // Crear un marcador para cada objeto en el array
    //     var marker = L.marker(markers[i].latlng, {icon: iconMap}).addTo(map);
    //     // Añadir un popup al marcador
    //     marker.bindPopup(markers[i].text).openPopup();
    // }

});