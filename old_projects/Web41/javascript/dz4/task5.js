const prompt = require('prompt-sync')();

function sovChislo(num) {
    if (num <= 1) return false;
    let sum = 0;
    for (let i = 1; i <= num / 2; i++) {
        if (num % i === 0) {
            sum += i;
        }
    }
    return sum === num;
}
const userInput = prompt('введите число для проверки:');
const number = parseInt(userInput,10);

if (sovChislo(number)) {
    console.log(`${number} является совершенным числом`);

} else {
    console.log(`${number} не является совершенным числом`);
}
