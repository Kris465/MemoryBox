const prompt = require('prompt-sync')();

function gcd(a, b) {
    if (b === 0) {
        return a;
    }
    return gcd(b, a % b);
}

const aInput = prompt('Введите первое число: ');
const bInput = prompt('Введите второе число: ');

const a = parseInt(aInput, 10);
const b = parseInt(bInput, 10);

if (isNaN(a) || isNaN(b)) {
    console.log('Пожалуйста, введите корректные целые числа.');
} else {
    const result = gcd(a, b);
    console.log(`Наибольший общий делитель ${a} и ${b} равен ${result}`);
}
