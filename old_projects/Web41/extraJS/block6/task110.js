const prompt = require('prompt-sync')(); 

const numStr = prompt("Введите натуральное число:");
const digits = numStr.split('');
const num = Number(numStr);
const len = digits.length;

const reversedNumStr = digits.slice().reverse().join('');
const reversedNum = Number(reversedNumStr);

const doublePadNumStr = '2' + numStr + '2';
const doublePadNum = Number(doublePadNumStr);

const digitToRemove = prompt("Введите цифру для удаления:");
const removedDigitsStr = digits.filter(d => d !== digitToRemove).join('');
const removedDigitsNum = removedDigitsStr === '' ? 0 : Number(removedDigitsStr);

let swappedNumStr;
if (len > 1) {
    const firstDigit = digits[0];
    const lastDigit = digits[len - 1];
    const middleDigits = digits.slice(1, len - 1);
    swappedNumStr = lastDigit + middleDigits.join('') + firstDigit;
} else {
    swappedNumStr = numStr;
}
const swappedNum = Number(swappedNumStr);

const doubledNumStr = numStr + numStr;
const doubledNum = Number(doubledNumStr);

console.log("а) число, прочитанное справа налево:", reversedNum);
console.log("б) число с приписанными по двойке в начало и конец:", doubledNum);
console.log("в) число после удаления всех цифр", digitToRemove, ":", removedDigitsNum);
console.log("г) число после перестановки первой и последней цифр:", swappedNum);
console.log("д) число, образованное из исходного приписыванием его самого:", doubledNum);