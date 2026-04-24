const prompt = require('prompt-sync')();

function analyzeNumber(number) {
    if (number < 100 || number > 999) {
        console.log("Пожалуйста, введите трехзначное число.");
        return;
    }

    const numStr = number.toString();

    const allSame = numStr[0] === numStr[1] && numStr[1] === numStr[2];
    console.log(`Все цифры одинаковые: ${allSame}`);

    const digits = new Set(numStr); 
    const hasDuplicates = digits.size < numStr.length;
    console.log(`Есть одинаковые цифры: ${hasDuplicates}`);
}

let number = parseInt(prompt("Введите трехзначное число:"));
if (!isNaN(number)) {
    analyzeNumber(number);
} else {
    console.log("Пожалуйста, введите корректное число.");
}