document.addEventListener("DOMContentLoaded", function() {
    var token = localStorage.getItem('token');
    var usuario_id = localStorage.getItem('usuario_id');
    
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    const messagesContainer = document.getElementById('chat-messages');

    // Conectar al WebSocket
    const socket = io.connect('http://127.0.0.1:5000');

    // Event listener para el botón de enviar
    sendButton.addEventListener('click', sendMessage);

    // Permitir enviar el mensaje al presionar Enter
    messageInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            sendMessage();
        }
    });

    function sendMessage() {
        const messageText = messageInput.value;
        if (messageText.trim() !== '') {
            socket.emit('message', {
                id_usuario: usuario_id,
                token: token,
                contenido: messageText
            });

            messageInput.value = '';
        }
    }

    // Cuando se recibe un mensaje a través del WebSocket
    socket.on('message', function(data) {
        const messageElement = document.createElement('div');
        messageElement.classList.add('message');
        messageElement.textContent = data.contenido;
        messagesContainer.appendChild(messageElement);
        messagesContainer.scrollTop = messagesContainer.scrollHeight;
    });
});
