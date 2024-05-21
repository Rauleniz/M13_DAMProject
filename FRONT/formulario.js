document.getElementById('post-profile-form').addEventListener('submit', function(event) {
    event.preventDefault(); 

    var formData = new FormData(event.target);
    var data = {};

    // Llenar el objeto data con los datos del formulario
    formData.forEach(function(value, key) {
        data[key] = value;
    });

    // Envía los datos al servidor
    fetch('http://127.0.0.1:5000/post/usuario', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)

    }).then(function(response) {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Error: ' + response.status + ' ' + response.statusText);
        }
    }).then(function(data) {
        console.log('Success:', data);
        window.location.href = 'bienvenida.html';

    }).catch(function(error) {
        console.error('Error:', error);
        alert('Error al dar de alta: ' + error.message);
    });
});
