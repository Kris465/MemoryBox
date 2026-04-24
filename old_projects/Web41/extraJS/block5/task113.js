const prompt = require('prompt-sync')();

function removeCharacterS(sentence) {
    return sentence.replace(/с/gi, ''); 
}

let userInput = prompt("Введите предложение:");
let result = removeCharacterS(userInput);
console.log("Результат:", result);