const prompt = require('prompt-sync')(); 

const numberInput = prompt("Введите натуральное число:");
const number = parseInt(numberInput, 10);

if (isNaN(number) || number <= 0) {
    console.log("Некорректный ввод");
} else {
    const digits = number.toString().split('');
    let isNonDecreasingFromLeft = true;
    for (let i = 0; i < digits.length - 1; i++) {
        if (parseInt(digits[i]) > parseInt(digits[i + 1])) {
            isNonDecreasingFromLeft = false;
            break;
        }
    }
    console.log(`Последовательность цифр числа при просмотре слева направо ${isNonDecreasingFromLeft ? 'упорядочена по неубыванию' : 'не упорядочена по неубыванию'}`);
}