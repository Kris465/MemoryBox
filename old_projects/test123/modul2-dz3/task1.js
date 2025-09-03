const prompt = require('prompt-sync')(); 


function stringStatistics(inputString) {
    let letterCount = 0;
    let digitCount = 0;
    let otherCount = 0;

    for (let char of inputString) {
        if (/[a-zA-Z]/.test(char)) {
            letterCount++;
        } else if (/[0-9]/.test(char)) {
            digitCount++;
        } else {
            otherCount++;
        }
    }

    console.log(`Количество букв: ${letterCount}`);
    console.log(`Количество цифр: ${digitCount}`);
    console.log(`Количество других знаков: ${otherCount}`);
}

const text = prompt('Введите строку: ');
stringStatistics(text);