const prompt = require('prompt-sync')();

function removeCharacters(sentence, n1, n2) {
    if (n1 < 0 || n2 < 0 || n1 >= sentence.length || n2 >= sentence.length || n1 > n2) {
        return "Некорректные значения индексов.";
    }
    return sentence.slice(0, n1) + sentence.slice(n2 + 1);
}

let userInput = prompt("Введите предложение:");
let n1 = parseInt(prompt("Введите начальный индекс (n1):"));
let n2 = parseInt(prompt("Введите конечный индекс (n2):"));

let result = removeCharacters(userInput, n1, n2);
console.log("Результат:", result);