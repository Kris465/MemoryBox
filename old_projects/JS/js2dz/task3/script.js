document.getElementById('threeDigitButton').addEventListener('click', function() {
    const threeDigitNumber = document.getElementById('threeDigitInput').value;
    const threeDigitResult = document.getElementById('threeDigitResult');
    
    if (threeDigitNumber.length === 3) {
        const digits = threeDigitNumber.split('');
        const hasDuplicates = new Set(digits).size !== digits.length;

        if (hasDuplicates) {
            threeDigitResult.textContent = 'В числе есть одинаковые цифры.';
        } else {
            threeDigitResult.textContent = 'В числе нет одинаковых цифр.';
        }
    } else {
        threeDigitResult.textContent = 'Введите трехзначное число.';
    }
});
    