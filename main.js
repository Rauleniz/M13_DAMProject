function initMap(){

    // contenido de las etiquetas:
    const tag_content = {
        img: '',
        username: '',
        description: '',
        links: '',
        song: '',
        address: ''
    }


    //centramos el mapa en un lugar específico (Barcelona)
    const centerMap = {lat: 41.3926386, lng: 2.0577881}

    //determinamos por defecto la posición de la ventana del mapa en nuestro navegador
    const mapOptions = {
        center: centerMap,
        zoom: 10,
        disableDefaultUI: true
    }


    // creamos nuevo objeto de google maps
    const map = new google.maps.Map(document.getElementById('google-map'), mapOptions)
}