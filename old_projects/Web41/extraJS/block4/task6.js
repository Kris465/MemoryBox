const prompt = require('prompt-sync')();

let num1 = prompt('введите 1-е число:');
let num2 = prompt('введите 2-е число:');

function compareNumbers(num1, num2)
 {
    if (num1 > num2) {
        console.log(`${num1} больше, чем ${num2}`);
        console.log(`${num2} меньше, чем ${num1}`);
    } else if (num1 < num2) {
        console.log(`${num2} больше, чем ${num1}`);
        console.log(`${num1} меньше, чем ${num2}`);
    } else {
        console.log("Числа равны, но они должны быть различными.");
    }
}


compareNumbers(num1, num2);