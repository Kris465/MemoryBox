const prompt = require('prompt-sync')();

function swapAdjacentLetters(word) {
    let letters = word.split('');
    
    for (let i = 0; i < letters.length; i += 2) {
        if (i + 1 < letters.length) {
            let temp = letters[i];
            letters[i] = letters[i + 1];
            letters[i + 1] = temp;
        }
    }

    return letters.join('');
}

let userInput = prompt("Введите слово из четного числа букв:");
if (userInput.length % 2 === 0) {
    let result = swapAdjacentLetters(userInput);
    console.log(result);
} else {
    console.log("Слово должно содержать четное число букв.");
}