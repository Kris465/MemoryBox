document.getElementById('myForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const digitsInput = document.getElementById('digits').value;
    const lettersInput = document.getElementById('letters').value;
    const uppercaseInput = document.getElementById('uppercase').value;

    const onlyDigitsRegex = /^\d+$/;
    const onlylettersRegex = /^[a-zA-Z]+$/;
    const onlyUppercaseRegex = /^[A-Z]+$/;

    if (!onlyDigitsRegex.test(digitsInput)) {
        alert("Поле должно содержать только цифры!");
    } else if (!onlylettersRegex.test(lettersInput)) {
        alert("Поле должно содержать только буквы!");
    } else if (!onlyUppercaseRegex.test(uppercaseInput)) {
        alert("Поле должно содержать только заглавные буквы!");
    } else {
        alert("Все поля валидны!");
    }
});