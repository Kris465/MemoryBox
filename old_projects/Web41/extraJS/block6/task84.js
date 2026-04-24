const prompt = require('prompt-sync')(); 

const numStr = prompt("Введите натуральное число, в котором все цифры различны:");


let maxDigit = -1;
let minDigit = 10;
let maxIndex = -1;
let minIndex = -1;


for (let i = 0; i < numStr.length; i++) {
    const digit = parseInt(numStr[i], 10);
    if (digit > maxDigit) {
        maxDigit = digit;
        maxIndex = i;
    }
    if (digit < minDigit) {
        minDigit = digit;
        minIndex = i;
    }
}


if (maxIndex < minIndex) {
    console.log("Максимальная цифра расположена левее минимальной.");
} else if (maxIndex > minIndex) {
    console.log("Минимальная цифра расположена левее максимальной.");
} else {
   
    console.log("Ошибка: максимальная и минимальная цифра расположены в одной позиции.");
}