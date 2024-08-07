function validateForm() {
    const username = document.getElementById('username').value;

    // Проверка на корректность логина
    const usernamePattern = /^(?![0-9])[a-zA-Z0-9]+$/;
    if (!usernamePattern.test(username)) {
        alert("Логин должен содержать только латиницу и цифры, при этом цифра не может быть первой.");
        return false;
    }

    const formData = new FormData(document.getElementById('userForm'));

    fetch('process.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('message').innerHTML = data;
        document.getElementById('userForm').style.display = 'none'; // Скрываем форму
    })
    .catch(error => console.error('Ошибка:', error));

    return false;
}