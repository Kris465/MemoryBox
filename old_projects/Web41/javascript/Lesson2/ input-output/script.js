document.getElementById('greetButton').addEventListener('click', function() {
    const name = document.getElementById('nameInput').value;
    if (name) {
        document.getElementById('greeting').innerText = `Привет, ${name}!`;
    } else {
        alert('Пожалуйста, введите ваше имя.');
    }
});
