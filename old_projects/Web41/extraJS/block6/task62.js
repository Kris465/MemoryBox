const prompt = require('prompt-sync')();  

const sequence = [];
while (true) {
    const input = prompt("Введите целое число (или 10000 для завершения):");
    const num = parseInt(input, 10);
    if (isNaN(num)) {
        alert("Некорректный ввод, попробуйте снова.");
        continue;
    }
    sequence.push(num);
    if (num === 10000) {
        break;
    }
}

const nInput = prompt("Введите число n:");
const n = parseInt(nInput, 10);
if (isNaN(n)) {
    console.log("Некорректный ввод числа n.");
} else {

    let position = -1;
    for (let i = 0; i < sequence.length; i++) {
        if (sequence[i] > n) {
            position = i + 1; 
            break;
        }
    }
    if (position !== -1) {
        console.log(`Первое число, большее ${n}, — это элемент №${position} (${sequence[position - 1]}).`);
    } else {
        console.log(`В последовательности нет чисел, больших ${n}.`);
    }
}