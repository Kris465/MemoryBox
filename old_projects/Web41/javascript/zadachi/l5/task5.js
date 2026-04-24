const prompt = require('prompt-sync')();

function isPowerOfTwo(x) {
    if(x<=0) {
        return false;
    }
    if (x===1) {
        return true;
    }
    return isPowerOfTwo(x/2);
}

const userInput = prompt('Введите число для проверки, является ли оно степенью двойки:');

const number = parseInt(userInput, 10);

if(isNaN(number)) {
    console.log('Пожалуйста, введите корректное число.');
} else {
    const result = isPowerOfTwo(number);
    console.log(`${number} ${result ? 'является' : 'не является'} степенью двойки.`)
}