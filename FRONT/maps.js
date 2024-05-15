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

// B - etiqueta para conocer las coordena
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
map.on('click', function(e) {
    var popup = L.popup()
        .setLatLng(e.latlng)
        .setContent('<input type="text" id="popupText" placeholder="Escribe tu texto aquí..."><button onclick="saveMarker()">Guardar</button>' + e.latlng.toString())
        .openOn(map);
});

// GUARDAR LA NUEVA ETIQUETA EN EL BACKEND

function saveMarker() {
    var text = document.getElementById('popupText').value;
    var latlng = popup.getLatLng();
    var lat = latlng.lat;
    var lng = latlng.lng;

    // Crear el objeto con los datos del marcador
    var data = {lat: lat, lng: lng, text: text};

    // Enviar la petición POST al servidor
    fetch('/post/ubicacion', {
        method: 'POST',
        headers: {
            "Authorization": "Bearer " + localStorage.getItem('token'),
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
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
var markers = /* Aquí iría la respuesta del servidor */"";

for (var i = 0; i < markers.length; i++) {
    // Crear un marcador para cada objeto en el array
    var marker = L.marker(markers[i].latlng, {icon: iconMap}).addTo(map);
    // Añadir un popup al marcador
    marker.bindPopup(markers[i].text).openPopup();
}





