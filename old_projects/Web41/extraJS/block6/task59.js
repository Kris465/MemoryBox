const prompt = require('prompt-sync')();  

const sequence = [];
let input;

do {
    input = prompt("Введите целое число (или 100 для завершения):");
    const num = parseInt(input, 10);
    if (!isNaN(num)) {
        sequence.push(num);
    } else {
        alert("Некорректный ввод, попробуйте снова.");
    }
} while (sequence[sequence.length - 1] !== 100);

let index77 = -1;
for (let i = 0; i < sequence.length; i++) {
    if (sequence[i] === 77) {
        index77 = i;
        break;
    }
}

if (index77 !== -1) {
    console.log(`Число 77 есть в последовательности. Первый его порядковый номер: ${index77 + 1}.`);
} else {
    console.log("Число 77 в последовательности отсутствует.");
}