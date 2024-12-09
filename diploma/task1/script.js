document.getElementById('userForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    if (name === '' || email === '') {
        alert('Пожалуйста, заполните все поля.');
        return;
    }

    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        alert('Пожалуйста, введите корректный email.');
        return;
    }

    alert('Форма успешно отправлена!');
});