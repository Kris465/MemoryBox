const prompt = require('prompt-sync')();  

const sequence = [];
while (true) {
    const input = prompt("Введите целое число (или -1 для завершения):");
    const num = parseInt(input, 10);
    if (isNaN(num)) {
        alert("Некорректный ввод, попробуйте снова.");
        continue;
    }
    sequence.push(num);
    if (num === -1) {
        break;
    }
}

let indexDivisibleBy6 = -1;
for (let i = 0; i < sequence.length; i++) {
    if (sequence[i] !== -1 && sequence[i] % 6 === 0) {
        indexDivisibleBy6 = i;
        break;
    }
}

if (indexDivisibleBy6 !== -1) {
    console.log(`В последовательности есть число, кратное 6. Первый такой элемент — порядковый номер ${indexDivisibleBy6 + 1}.`);
} else {
    console.log("В последовательности нет чисел, кратных 6.");
}