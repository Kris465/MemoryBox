const prompt = require('prompt-sync')();

function createAbbreviation(phrase) {

    return phrase
        .split(' ')
        .map(word => word.charAt(0).toUpperCase())
        .join('');
}

const userInput = prompt("Введите словосочетание:");
const result = createAbbreviation(userInput);
console.log(`Аббревиатура: ${result}`);