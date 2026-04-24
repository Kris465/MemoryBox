const prompt = require('prompt-sync')(); 
const targetFactorial = parseInt(prompt("Введите известный факториал:"));

function findNumberByFactorial(fact) {
    if (fact < 1) {
        return fact === 1 ? 0 : -1; 
    }
    let n = 1;
    let currentFactorial = 1;
    while (currentFactorial < fact) {
        n++;
        currentFactorial *= n;
        if (currentFactorial === fact) {
            return n;
        }
    }
    return -1;
}

const n = findNumberByFactorial(targetFactorial);

if (n !== -1) {
    alert(`Число, факториал которого равен ${targetFactorial}, равно ${n}.`);
} else {
    alert(`Факториал числа ${n} не найден или значение некорректно.`);
}