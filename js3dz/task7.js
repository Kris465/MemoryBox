const prompt = require('prompt-sync')();

let numberStr = prompt('Введите число: ');
let shift = parseInt(prompt('На сколько цифр сдвинуть? '));

shift %= numberStr.length; // Чтобы избежать лишних сдвигов
let shiftedNumber = numberStr.slice(shift) + numberStr.slice(0, shift);

console.log(`Результат сдвига: ${shiftedNumber}`);
