const prompt = require('prompt-sync')(); 

const sequence = [];
while (true) {
    const input = prompt("Введите целое число (или отрицательное для завершения):");
    const num = parseInt(input, 10);
    if (isNaN(num)) continue;
    sequence.push(num);
    if (num < 0) break;
}

const firstElement = sequence[0];
const allEqual = sequence.every((value) => value === firstElement);

if (allEqual) {
    console.log("Все элементы последовательности равны между собой.");
} else {
    console.log("Не все элементы последовательности равны между собой.");
}