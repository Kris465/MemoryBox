

function reverseBetween(word, k, s) {
    if (word.length !== 15) {
        return "Слово должно содержать ровно 15 букв.";
    }
    if (k < 1 || s > 15 || k >= s) {
        return "Некорректные значения k и s.";
    }

    let firstPart = word.slice(0, k); 
    let middlePart = word.slice(k, s - 1).split('').reverse().join(''); 
    let lastPart = word.slice(s - 1); 

    return firstPart + middlePart + lastPart;
}

let userInput = prompt("Введите слово из 15 букв:");
let k = parseInt(prompt("Введите значение k (1-14):"));
let s = parseInt(prompt("Введите значение s (2-15):"));

let result = reverseBetween(userInput, k, s);
console.log(result);