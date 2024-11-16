document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Предотвращаем отправку формы

    const digitsInput = document.getElementById('digits').value;
    const lettersInput = document.getElementById('letters').value;
    const uppercaseInput = document.getElementById('uppercase').value;

    const onlyDigitsRegex = /^\d+$/;
    const onlyLettersRegex = /^[a-zA-Z]+$/;
    const onlyUppercaseLettersRegex = /^[A-Z]+$/;

    if (!onlyDigitsRegex.test(digitsInput)) {
        alert('Поле "Только цифры" должно содержать только цифры.');
    } else if (!onlyLettersRegex.test(lettersInput)) {
        alert('Поле "Только буквы" должно содержать только буквы.');
    } else if (!onlyUppercaseLettersRegex.test(uppercaseInput)) {
        alert('Поле "Только заглавные буквы" должно содержать только заглавные буквы.');
    } else {
        alert('Все поля валидны!');
    }
});
