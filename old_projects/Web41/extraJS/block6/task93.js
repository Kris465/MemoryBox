const prompt = require('prompt-sync')(); 

const days = prompt("Введите количество осадков за каждый день мая через пробел:").split(' ').map(Number);
const firstRainDay = days.findIndex(day => day > 0);
console.log(firstRainDay);