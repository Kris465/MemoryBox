const prompt = require('prompt-sync')(); 

const sequence = [];
for (let i = 0; i < 20; i++) {
    const input = prompt(`Введите натуральное число ${i + 1} из 20:`);
    const num = parseInt(input, 10);
    if (isNaN(num) || num <= 0) {
        alert("Некорректный ввод, попробуйте снова.");
        i--;
    } else {
        sequence.push(num);
    }
}

let pairIndex = -1;
for (let i = 0; i < sequence.length - 1; i++) {
    if (sequence[i] % 2 !== 0 && sequence[i + 1] % 2 !== 0) {
        pairIndex = i + 1;
        break;
    }
}

if (pairIndex !== -1) {
    console.log(`Первая пара соседних нечетных чисел — это числа с порядковыми номерами ${pairIndex} и ${pairIndex + 1}.`);
} else {
    console.log("В последовательности нет соседних нечетных чисел.");
}