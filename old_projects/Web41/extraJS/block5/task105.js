const prompt = require('prompt-sync')();

function reverseMiddleLetters(word) {
    if (word.length !== 12) {
        return "Слово должно содержать ровно 12 букв.";
    }

    let start = 2; 
    let end = 9;  

    let firstPart = word.slice(0, start);
    let middlePart = word.slice(start, end + 1).split('').reverse().join('');
    let lastPart = word.slice(end + 1);

    return firstPart + middlePart + lastPart;
}

let userInput = prompt("Введите слово из 12 букв:");
let result = reverseMiddleLetters(userInput);
console.log(result);