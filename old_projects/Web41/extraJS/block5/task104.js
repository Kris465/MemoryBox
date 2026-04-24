const prompt = require('prompt-sync')();

function swapHalves(word) {
    let length = word.length;
    let halfLength = length / 2;
    let firstHalf = word.slice(0, halfLength);
    let secondHalf = word.slice(halfLength);

    let swapped = '';

    for (let i = 0; i < halfLength; i++) {
        swapped += secondHalf[halfLength - 1 - i] + firstHalf[i];
    }

    return swapped;
}

let userInput = prompt("Введите слово из четного числа букв:");
if (userInput.length % 2 === 0) {
    let result = swapHalves(userInput);
    console.log(result);
} else {
    console.log("Слово должно содержать четное число букв.");
}