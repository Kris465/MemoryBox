document.querySelector('.send-button').addEventListener('click', function() {
    const input = document.querySelector('.message-input');
    const messageText = input.value;

    if (messageText.trim() !== '') {
        addMessage(messageText, 'Пользователь 2'); // Укажите имя пользователя
        input.value = ''; // Очистить поле ввода
    }
});

function addMessage(text, username) {
    const messagesContainer = document.getElementById('messages');

    // Создание нового элемента сообщения
    const messageElement = document.createElement('div');
    messageElement.classList.add('message', 'right'); // Добавляем класс 'right' для сообщений от пользователя

    // Создание элемента для аватара
    const avatarElement = document.createElement('img');
    avatarElement.src = 'path/to/avatar.jpg'; // Замените на путь к вашему аватару
    avatarElement.alt = "Аватар " + username; // Альтернативный текст для аватара
    avatarElement.classList.add('avatar'); // Добавьте класс для стилизации

    // Создание элемента для содержимого сообщения
    const messageContentElement = document.createElement('div');
    messageContentElement.classList.add('message-content');

    // Создание элемента для имени пользователя
    const usernameElement = document.createElement('span');
    usernameElement.classList.add('username');
    usernameElement.textContent = username;

    // Создание элемента для текста сообщения
    const textElement = document.createElement('p');
    textElement.textContent = text;

    // Создание элемента для времени
    const timestampElement = document.createElement('span');
    timestampElement.classList.add('timestamp');
    timestampElement.textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

    // Сборка структуры сообщения
    messageContentElement.appendChild(usernameElement);
    messageContentElement.appendChild(textElement);
    messageContentElement.appendChild(timestampElement);
    
    messageElement.appendChild(avatarElement);
    messageElement.appendChild(messageContentElement);

    // Добавление нового сообщения в контейнер
    messagesContainer.appendChild(messageElement);

    // Прокрутка вниз
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}
