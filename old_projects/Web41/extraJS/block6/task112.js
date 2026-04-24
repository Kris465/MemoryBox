const prompt = require('prompt-sync')(); 

const numberStr = prompt("Введите натуральное число:");
function findRightmost3Position(numStr) {
    for (let i = numStr.length - 1; i >= 0; i--) {
        if (numStr[i] === '3') {
            return numStr.length - i;
        }
    }
    return 0;
}
const position = findRightmost3Position(numberStr);
console.log(`Номер цифры 3 от конца: ${position}`);