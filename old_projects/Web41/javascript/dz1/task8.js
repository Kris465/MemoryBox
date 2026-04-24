const prompt = require('prompt-sync')();
let money = prompt("Введите сумму денег:");
let chocolate = 12;
let colvo = Math.floor(money/chocolate);
let ostatok = money % chocolate;
console.log(`Сколько вы можете купить шоколада: ${colvo}, у вас останется ${ostatok}`);
