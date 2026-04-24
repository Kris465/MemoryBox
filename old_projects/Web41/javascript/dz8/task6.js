const prompt = require('prompt-sync')();

function combineStrings(...strings) {
    return strings.join('');
}


let userInput;
let spisok = [];


while (userInput != 'stop') {
    userInput = prompt('Введите строку или stop: ');
    if (userInput === 'stop') {
        break;
    }
    spisok.push(userInput);
}

const result = combineStrings(spisok);
console.log(result);