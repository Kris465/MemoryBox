const prompt = require('prompt-sync')();


let a1 = parseInt(prompt("Введите первую цифру первого двузначного числа (десятки): "));
let a2 = parseInt(prompt("Введите вторую цифру первого двузначного числа (единицы): "));


let b1 = parseInt(prompt("Введите первую цифру второго двузначного числа (десятки): "));
let b2 = parseInt(prompt("Введите вторую цифру второго двузначного числа (единицы): "));


let numberA = a1 * 10 + a2;
let numberB = b1 * 10 + b2;


let sum = numberA + numberB;


let tens = Math.floor(sum / 10); 
let units = sum % 10; 


console.log(`Сумма: ${sum}`);
console.log(`Десятки: ${tens}, Единицы: ${units}`);