const prompt = require('prompt-sync')();

function factorial(num) {
    if (num < 0) {
        return
    } 

    if (num == 0) {
        return 1;
    }

    return num * factorial(num - 1);
}

let num = prompt('введите число:');
const result = factorial(num);
console.log(`факториал числа: ${result}`);
  