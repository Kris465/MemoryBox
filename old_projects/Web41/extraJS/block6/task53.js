const prompt = require('prompt-sync')(); 

const numberInput = prompt("Введите натуральное число:");
const number = parseInt(numberInput, 10);

if (isNaN(number) || number <= 0) {
    console.log("Некорректный ввод");
} else {
    const digits = number.toString().split('');
    let isAscendingFromRight = true;
    for (let i = 0; i < digits.length - 1; i++) {
        if (parseInt(digits[i]) <= parseInt(digits[i + 1])) {
            isAscendingFromRight = false;
            break;
        }
    }
    console.log(`Последовательность цифр числа при просмотре справа налево ${isAscendingFromRight ? 'упорядочена по возрастанию' : 'не упорядочена по возрастанию'}`);
}