const prompt = require('prompt-sync')(); 
const sequence = [];
while (true) {
    const input = prompt("Введите целое число (или -1 для завершения):");
    const num = parseInt(input, 10);
    if (isNaN(num)) {
        console.log(`Некорректный ввод, попробуйте снова.`);
        continue;
    }
    sequence.push(num);
    if (num === -1) {
        break;
    }
}

let pairIndex = -1;
for (let i = 0; i < sequence.length - 1; i++) {
    if (sequence[i] === sequence[i + 1]) {
        pairIndex = i + 1;
        break;
    }
}

if (pairIndex !== -1) {
    console.log(`Первая пара одинаковых соседних чисел — это числа с порядковыми номерами ${pairIndex} и ${pairIndex + 1}.`);
} else {
    console.log("В последовательности нет соседних одинаковых чисел.");
}