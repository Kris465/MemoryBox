const prompt = require('prompt-sync')();

function numberToWords(num) {
    if (num < 10 || num >= 100) {
        return "Число должно быть двузначным";
    }

    const units = ["", "один", "два", "три", "четыре", "пять", 
                   "шесть", "семь", "восемь", "девять"];
    const teens = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", 
                   "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"];
    const tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", 
                  "шестьдесят", "семьдесят", "восемьдесят", "девяносто"];

    if (num >= 10 && num < 20) {
        return teens[num - 10];
    } else {
        const ten = Math.floor(num / 10);
        const unit = num % 10;
        return (tens[ten] + " " + units[unit]).trim();
    }
}


const input = prompt("Введите двузначное число: ");
const number = parseInt(input);


if (isNaN(number)) {
    console.log("Ошибка: введено не число.");
} else {
    const result = numberToWords(number);
    console.log(result);
}