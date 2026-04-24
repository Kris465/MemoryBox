const prompt = require('prompt-sync')(); 

const sequence = [1.2, -2.5, 3.7, -4.8, 5.9, 6.1, -7.3, 8.4, 9.6, -10.7, 11.8, 12.9, -13.0, 14.2, 15.3];

let firstNegativeIndex = -1;

for (let i = 0; i < sequence.length; i++) {
    if (sequence[i] < 0) {
        firstNegativeIndex = i;
        break;
    }
}

if (firstNegativeIndex !== -1) {
    console.log(`В последовательности есть отрицательное число. Первый отрицательный элемент — порядковый номер ${firstNegativeIndex + 1}.`);
} else {
    console.log("В последовательности нет отрицательных чисел.");
}