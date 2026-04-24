const prompt = require('prompt-sync')();

function checkDigits(number, a) {

    if (number < 10 || number > 99) {
        console.log("Введите двузначное число.");
        return;
    }

    
    const tens = Math.floor(number / 10); 
    const units = number % 10; 

 
    const containsThree = (tens === 3 || units === 3);

    const containsA = (tens === a || units === a);


    console.log(`Цифра 3 ${containsThree ? "входит" : "не входит"} в число ${number}.`);
    console.log(`Цифра ${a} ${containsA ? "входит" : "не входит"} в число ${number}.`);
}


const number = parseInt(prompt("Введите двузначное число:"));

const a = parseInt(prompt("Введите цифру a (0-9):"));

if (a < 0 || a > 9) {
    console.log("Цифра a должна быть от 0 до 9.");
} else {
    checkDigits(number, a);
}