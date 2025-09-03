const prompt = require('prompt-sync')();

function reverseNumber(n) {
    if (n < 10) {
        return n.toString();
    }
    
    return (n % 10).toString() + reverseNumber(Math.floor(n / 10));
}

const userInput = prompt('Введите число для вывода справа налево: ');

const number = parseInt(userInput, 10);

if (isNaN(number)) {
    console.log('Пожалуйста, введите корректное число.');
} else {
    const reversed = reverseNumber(number);
    console.log(`Число ${number} справа налево: ${reversed}`);
}
