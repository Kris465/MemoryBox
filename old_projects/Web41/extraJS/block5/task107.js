const prompt = require('prompt-sync')();

function swapAandO(word) {
    let firstAIndex = word.indexOf('а');
    let lastOIndex = word.lastIndexOf('о');

    if (firstAIndex === -1 || lastOIndex === -1) {
        return "Не найдено необходимое количество букв 'а' или 'о'.";
    }

    let letters = word.split('');

    let temp = letters[firstAIndex];
    letters[firstAIndex] = letters[lastOIndex];
    letters[lastOIndex] = temp;

    return letters.join('');
}

let userInput = prompt("Введите слово:");
let result = swapAandO(userInput);
console.log(result);