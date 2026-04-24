const prompt = require('prompt-sync')(); 

const numStr = prompt("Введите натуральное число:");
const a = prompt("Введите цифру a:");
const b = prompt("Введите цифру b:");

const indexA = numStr.lastIndexOf(a);
const indexB = numStr.lastIndexOf(b);

if (indexA === -1 && indexB === -1) {
    console.log("В числе нет ни цифры " + a + ", ни цифры " + b + ".");
} else if (indexA !== -1 && indexB !== -1) {
    if (indexA > indexB) {
        console.log("Цифра " + a + " расположена правее, чем цифра " + b + ".");
    } else if (indexB > indexA) {
        console.log("Цифра " + b + " расположена правее, чем цифра " + a + ".");
    } else {
        console.log("Цифры " + a + " и " + b + " расположены в одной позиции.");
    }
} else if (indexA !== -1) {
    console.log("В числе есть цифра " + a + ", а цифра " + b + " отсутствует.");
} else {
    console.log("В числе есть цифра " + b + ", а цифра " + a + " отсутствует.");
}