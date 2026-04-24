const prompt = require('prompt-sync')();
let chislo = prompt("Введите трехзначное число:")
let number1 = chislo % 10
let number2 = Math.floor((chislo % 100) / 10) 
let number3 = Math.floor(chislo / 100)
console.log(number1,number2,number3)