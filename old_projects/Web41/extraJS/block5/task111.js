const prompt = require('prompt-sync')();

function removeMiddleLetters(word) {
    let length = word.length;
    if (length % 2 === 1) {
        let middleIndex = Math.floor(length / 2);
        return word.slice(0, middleIndex) + word.slice(middleIndex + 1);
    } else {
        let middleIndex1 = length / 2 - 1;
        let middleIndex2 = length / 2;
        return word.slice(0, middleIndex1) + word.slice(middleIndex2 + 1);
    }
}

let userInput = prompt("Введите слово:");
let result = removeMiddleLetters(userInput);
console.log("Результат:", result);