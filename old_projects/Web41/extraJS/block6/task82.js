const numStr = prompt("Введите натуральное число:");

// Находим максимальную и минимальную цифру в числе
let maxDigit = 0;
let minDigit = 9;

for (let digit of numStr) {
    const d = parseInt(digit, 10);
    if (d > maxDigit) maxDigit = d;
    if (d < minDigit) minDigit = d;
}

// Проверяем, является ли разность четным числом
const difference = maxDigit - minDigit;
if (difference % 2 === 0) {
    console.log("Разность максимальной и минимальной цифр является четным числом.");
} else {
    console.log("Разность максимальной и минимальной цифр не является четным числом.");
}