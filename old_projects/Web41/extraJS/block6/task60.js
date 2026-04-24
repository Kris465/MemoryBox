const prompt = require('prompt-sync')();  
const sequence = [];
for (let i = 0; i < 20; i++) {
    const input = prompt(`Введите натуральное число ${i + 1} из 20:`);
    const num = parseInt(input, 10);
    if (isNaN(num) || num <= 0) {
        console.log(`Некорректный ввод, попробуйте снова.`);
        i--; 
    } else {
        sequence.push(num);
    }
}

let indexEndingWith7 = -1;
for (let i = 0; i < sequence.length; i++) {
    const lastDigit = sequence[i] % 10;
    if (lastDigit === 7) {
        indexEndingWith7 = i;
        break;
    }
}

if (indexEndingWith7 !== -1) {
    console.log(`В последовательности есть число, оканчивающееся на 7. Первый такой элемент — порядковый номер ${indexEndingWith7 + 1}.`);
} else {
    console.log("В последовательности нет чисел, оканчивающихся на 7.");
}