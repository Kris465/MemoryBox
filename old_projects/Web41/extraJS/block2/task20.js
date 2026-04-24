const prompt = require('prompt-sync')();
let number = 5434; 


let reversed = parseInt(number.toString().split('').reverse().join(''), 10);
console.log("a) Число, полученное при прочтении справа налево:", reversed);


let strNumber = number.toString();
let rearranged = strNumber[1] + strNumber[0] + strNumber[3] + strNumber[2];
console.log("b) Перестановка первой и второй, третьей и четвертой цифр:", parseInt(rearranged, 10));


let swapped23 = strNumber[0] + strNumber[2] + strNumber[1] + strNumber[3];
console.log("в) Перестановка второй и третьей цифр:", parseInt(swapped23, 10));


let firstDigit = strNumber[0];
let secondDigit = strNumber[1];
let thirdDigit = strNumber[2];
let fourthDigit = strNumber[3];

let rearrangedEnds = thirdDigit + fourthDigit + firstDigit + secondDigit;
console.log("г) Перестановка двух первых и двух последних цифр (с выделением):", parseInt(rearrangedEnds, 10));


let swappedEnds = strNumber.slice(2) + strNumber.slice(0, 2);
console.log("г) Перестановка двух первых и двух последних цифр (без выделения):", parseInt(swappedEnds, 10));
