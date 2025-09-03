const prompt = require('prompt-sync')(); 


function swapCaseAndReplaceDigits(inputString) {
    let result = '';

    for (let char of inputString) {
        if (/[A-Z]/.test(char)) {
            result += char.toLowerCase();
        } else if (/[a-z]/.test(char)) {
            result += char.toUpperCase();
        } else if (/[0-9]/.test(char)) {
            result += '_';
        } else {
            result += char;
        }
    }
    return result;
}

const text = prompt("Введите текст: ")
const modifiedString = swapCaseAndReplaceDigits(text);
console.log(modifiedString); 
