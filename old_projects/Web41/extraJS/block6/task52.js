const prompt = require('prompt-sync')(); 

const numberInput = prompt("Введите натуральное число:");
const number = parseInt(numberInput, 10);

if (isNaN(number) || number <= 1) {
    console.log("Некорректный ввод или число не является простым");
} else {
    let isPrime = true;
    for (let i = 2; i <= Math.sqrt(number); i++) {
        if (number % i === 0) {
            isPrime = false;
            break;
        }
    }
    console.log(`Число ${number} ${isPrime ? 'является' : 'не является'} простым`);
}