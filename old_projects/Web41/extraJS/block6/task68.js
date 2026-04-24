const prompt = require('prompt-sync')(); 

const sequence = [];
while (true) {
    const input = prompt("Введите целое число (или 9999 для завершения):");
    const num = parseInt(input, 10);
    if (isNaN(num)) {
        alert("Некорректный ввод, попробуйте снова.");
        continue;
    }
    sequence.push(num);
    if (num === 9999) {
        break;
    }
}

let pairIndex = -1;
for (let i = 0; i < sequence.length - 1; i++) {
    if (sequence[i] % 2 === 0 && sequence[i + 1] % 2 === 0) {
        pairIndex = i + 1;
        break;
    }
}

if (pairIndex !== -1) {
    console.log(`Первая пара соседних четных чисел — это числа с порядковыми номерами ${pairIndex} и ${pairIndex + 1}.`);
} else {
    console.log("В последовательности нет соседних четных чисел.");
}