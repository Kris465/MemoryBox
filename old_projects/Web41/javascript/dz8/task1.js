const prompt = require('prompt-sync')();

function stringStatistics(str) {
    let letterCount = 0;
    let digitCount = 0;
    let otherCount = 0;

    for (let char of str) {
        if (/[a-zA-Zа-яА-ЯёЁ]/.test(char)) { 
            letterCount++;
        } else if (/[0-9]/.test(char)) { 
            digitCount++;
        } else {
            otherCount++; 
        }
    }

    return {
        letters: letterCount,
        digits: digitCount,
        others: otherCount
    };
}


const stroka = prompt("введите строчку: ");

const stats = stringStatistics(stroka);
console.log(`Количество букв: ${stats.letters}`);
console.log(`Количество цифр: ${stats.digits}`);
console.log(`Количество других знаков: ${stats.others}`);



