const prompt = require('prompt-sync')();

let num1 = prompt('введите 1-е число:');
let num2 = prompt('введите 2-е число:');

function findMaxMin(num1, num2) {
    let max, min;

    if (num1 > num2) {
        max = num1;
        min = num2;
    } else {
        max = num2;
        min = num1;
    }

    return { max, min };
}



const result = findMaxMin(num1, num2);
console.log(`Максимальное значение: ${result.max}`);
console.log(`Минимальное значение: ${result.min}`);