
const firstNumber = parseFloat(prompt("Введите первое число:"));
const secondNumber = parseFloat(prompt("Введите второе число:"));

const sqrtSecond = Math.sqrt(secondNumber);

if (sqrtSecond < firstNumber) {
    secondNumber *= 5;
}

console.log(`Первое число: ${firstNumber}`);
console.log(`Второе число (после возможного увеличения): ${secondNumber}`);