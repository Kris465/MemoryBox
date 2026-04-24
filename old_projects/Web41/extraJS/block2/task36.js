const prompt = require('prompt-sync')();

let c1 = parseInt(prompt("Введите первую цифру трехзначного числа (сотни): "));
let c2 = parseInt(prompt("Введите вторую цифру трехзначного числа (десятки): "));
let c3 = parseInt(prompt("Введите третью цифру трехзначного числа (единицы): "));


let d1 = parseInt(prompt("Введите первую цифру двузначного числа (десятки): "));
let d2 = parseInt(prompt("Введите вторую цифру двузначного числа (единицы): "));


let numberC = c1 * 100 + c2 * 10 + c3; 
let numberD = d1 * 10 + d2; 


let sum = numberC + numberD;


let hundreds = Math.floor(sum / 100); 
let tens = Math.floor((sum % 100) / 10); 
let units = sum % 10; 

// Выводим результат
console.log(`Сумма: ${sum}`);
console.log(`Сотни: ${hundreds}, Десятки: ${tens}, Единицы: ${units}`);