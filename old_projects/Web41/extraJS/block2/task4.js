const prompt = require('prompt-sync')();


const meters = parseFloat(prompt("Введите метры:"));
const kilometers = Math.floor(meters / 1000);

console.log(`${kilometers}`);