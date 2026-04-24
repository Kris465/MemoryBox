const prompt = require('prompt-sync')();

function removeOddPositionO(sentence) {
    let result = '';
    for (let i = 0; i < sentence.length; i++) {
        if (sentence[i] === 'о' && i % 2 !== 0) {
            continue;
        }
        result += sentence[i];
    }
    return result;
}

let userInput = prompt("Введите предложение:");
let result = removeOddPositionO(userInput);
console.log("Результат:", result);