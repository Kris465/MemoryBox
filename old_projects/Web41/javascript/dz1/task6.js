const prompt = require('prompt-sync')();
let dollar = prompt('введите количество долларов: ');
const skolko = 0.95;
let euro = dollar * skolko;
console.log(`столько доллров в евро ${euro}`);