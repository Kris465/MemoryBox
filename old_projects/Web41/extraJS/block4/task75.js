
console.log(`Результат: ${firstNumber}`);

function absoluteValue(num) {
    return (num * (num >= 0)) + (-num * (num < 0));
}


function halfSumOfAbsoluteValues(a, b) {
    const absA = absoluteValue(a);
    const absB = absoluteValue(b);
    return (absA + absB) / 2;
}


function sqrtOfProductOfAbsoluteValues(a, b) {
    const absA = absoluteValue(a);
    const absB = absoluteValue(b);
    return Math.sqrt(absA * absB);
}


const num1 = parseFloat(prompt("Введите первое вещественное число:"));
const num2 = parseFloat(prompt("Введите второе вещественное число:"));


const halfSum = halfSumOfAbsoluteValues(num1, num2);
console.log(`Полусумма абсолютных величин: ${halfSum}`);


const sqrtProduct = sqrtOfProductOfAbsoluteValues(num1, num2);
console.log(`Квадратный корень из произведения абсолютных величин: ${sqrtProduct}`);