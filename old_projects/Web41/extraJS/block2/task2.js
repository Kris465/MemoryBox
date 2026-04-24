const prompt = require('prompt-sync')();

const kg = prompt('введите кол-во кг:');
const cent = Math.floor(kg / 100);

console.log(`ответ: ${cent}`);
