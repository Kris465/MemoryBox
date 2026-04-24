const prompt = require('prompt-sync')();

const priceCandy = prompt("введите цену за 1кг конфет: ");
const priceCookies = prompt("введите цену за 1 кг печенья: ");
const priceApples = prompt("введте цену за 1 кг яблок: ");

const x = prompt("введите сколько купили: "); 
const y = prompt("введите сколько купили: "); 
const z = prompt("введите сколько купили: "); 

const totalCost = (x * priceCandy) + (y * priceCookies) + (z * priceApples);

console.log(`Общая стоимость покупки: ${totalCost} рублей`);