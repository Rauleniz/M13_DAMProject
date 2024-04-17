function initMap(){

    //centramos el mapa en un lugar específico (Barcelona)
    const centerMap = {lat: 41.3926386, long: 2.0577881}

    //determinamos por defecto la posición de la ventana del mapa en nuestro navegador
    const mapOption = {
        center: centerMap,
        zoom: 10
    }


    // creamos nuevo objeto de google maps
    const map = new google.maps.Map(document.getElementById('google-map'), mapOptions)
}