document.getElementById('si-btn').addEventListener('click', function() {
    var usuario_id = localStorage.getItem('usuario_id'); 
    var token = localStorage.getItem('token'); 

    fetch("http://127.0.0.1:5000/delete/plan/" + usuario_id, {
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
        },
        mode: 'cors'
    })
    .then(response => response.json())
    .then(data => {
        console.log("Plan cancelado:", data);
        alert("Plan cancelado:", data)
        window.location.href = "index.html";
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById('no-btn').addEventListener('click', function() {        
    window.location.href = "miperfil.html";
});
