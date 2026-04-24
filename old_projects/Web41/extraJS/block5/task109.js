const prompt = require('prompt-sync')();

function removeThirdLetter(word) {
    return word.slice(0, 2) + word.slice(3);
}

function removeKthLetter(word, k) {
    if (k < 1 || k > word.length) {
        return "Некорректное значение k.";
    }
    return word.slice(0, k - 1) + word.slice(k);
}

let userInput = prompt("Введите слово:");
let resultAfterRemovingThird = removeThirdLetter(userInput);
console.log("После удаления третьей буквы:", resultAfterRemovingThird);

let k = parseInt(prompt("Введите номер буквы для удаления (k):"));
let resultAfterRemovingKth = removeKthLetter(userInput, k);
console.log("После удаления k-й буквы:", resultAfterRemovingKth);