const prompt = require('prompt-sync')();

function removeFirstO(word) {
    let index = word.indexOf('о');
    if (index !== -1) {
        return word.slice(0, index) + word.slice(index + 1);
    }
    return word;
}

function removeLastL(word) {
    let index = word.lastIndexOf('л');
    if (index !== -1) {
        return word.slice(0, index) + word.slice(index + 1);
    }
    return word;
}

let userInput = prompt("Введите слово:");
let resultAfterRemovingFirstO = removeFirstO(userInput);
console.log("После удаления первой буквы 'о':", resultAfterRemovingFirstO);

let resultAfterRemovingLastL = removeLastL(resultAfterRemovingFirstO);
console.log("После удаления последней буквы 'л':", resultAfterRemovingLastL);