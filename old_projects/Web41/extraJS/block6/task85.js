const prompt = require('prompt-sync')(); 

const numStr = prompt("Введите натуральное число:");
const index2 = numStr.indexOf('2');
const index5 = numStr.indexOf('5');

if (index2 === -1 && index5 === -1) {
    console.log("В числе нет ни цифры 2, ни цифры 5.");
} else if (index2 !== -1 && index5 !== -1) {
    if (index2 < index5) {
        console.log("Цифра 2 расположена левее цифры 5.");
    } else if (index5 < index2) {
        console.log("Цифра 5 расположена левее цифры 2.");
    } else {
        console.log("Цифры 2 и 5 расположены в одной позиции.");
    }
} else if (index2 !== -1) {
    console.log("В числе есть цифра 2, а цифра 5 отсутствует.");
} else {
    console.log("В числе есть цифра 5, а цифра 2 отсутствует.");
}