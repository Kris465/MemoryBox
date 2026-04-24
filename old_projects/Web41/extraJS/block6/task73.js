const prompt = require('prompt-sync')(); 

const sequence = [];
for (let i = 0; i < 15; i++) {
    const num = parseInt(prompt(`Введите целое число ${i + 1}:`), 10);
    sequence.push(num);
}

const allEqual = sequence.every((value, index, arr) => value === arr[0]);

if (allEqual) {
    console.log("Все элементы последовательности равны между собой.");
} else {
    console.log("Не все элементы последовательности равны между собой.");
}