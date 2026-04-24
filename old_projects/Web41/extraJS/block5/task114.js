const prompt = require('prompt-sync')();

function removeDuplicateLetters(word) {
    let result = '';
    for (let char of word) {
        if (!result.includes(char)) {
            result += char;
        }
    }
    return result;
}

let userInput = prompt("Введите слово:");
let result = removeDuplicateLetters(userInput);
console.log("Результат:", result);