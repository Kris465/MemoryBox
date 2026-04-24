console.log(`Результат: ${firstNumber}`);

function absoluteValue(num) {
    return (num * (num >= 0)) + (-num * (num < 0));
}

if (absFirst > absSecond) {
    firstNumber /= 2;
}
const firstNumber = parseFloat(prompt("Введите первое число:"));
const secondNumber = parseFloat(prompt("Введите второе число:"));

const absFirst = absoluteValue(firstNumber);
const absSecond = absoluteValue(secondNumber);

console.log(`Результат: ${firstNumber}`);