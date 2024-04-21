document.addEventListener("DOMContentLoaded", function() {
    const messageInput = document.getElementById('message-input');
    const sendButton = document.getElementById('send-button');
    const messagesContainer = document.getElementById('messages-container');

    // Event listener para el botón de enviar
    sendButton.addEventListener('click', function() {
        // Obtener el mensaje del input
        const messageText = messageInput.value;

        // Si el mensaje no está vacío
        if (messageText.trim() !== '') {
            // Crear un nuevo elemento para representar el mensaje
            const messageElement = document.createElement('div');
            messageElement.classList.add('message');
            messageElement.textContent = messageText;

            // Agregar el mensaje al contenedor de mensajes
            messagesContainer.appendChild(messageElement);

            // Limpiar el input
            messageInput.value = '';

            // Desplazarse automáticamente hacia abajo para mostrar el mensaje más reciente
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }
    });

    // Opcional: permitir enviar el mensaje al presionar Enter
    messageInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            sendButton.click();
        }
    });
});
