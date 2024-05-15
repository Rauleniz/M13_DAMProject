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

    iconSize:     [64, 64], // size of the icon
    iconAnchor:   [22, 94], // point of the icon which will correspond to marker's location
    popupAnchor:  [-3, -76] // point from which the popup should open relative to the iconAnchor
});

//A - añadir marcador (el tag)
// L.marker([41.39, 2.17],{draggable: true}).addTo(map);
L.marker([41.39, 2.17],{icon: iconMap}).addTo(map);

// B - añadir etiqueta
var popup = L.popup()
.setLatLng([41.3868115, 2.172877])
.setContent("Etiqueta: var popup")
.openOn(map);

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("Raúl\nEtiqueta Demo\nArtista" + e.latlng.toString())
        .openOn(map);
}

map.on('click', onMapClick);


