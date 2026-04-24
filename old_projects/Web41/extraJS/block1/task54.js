const prompt = require('prompt-sync')(); 

const num1 = Number(prompt('возвраст миты: '));
const num2 = Number(prompt('возвраст тани: '));

const voz = ( (num1 + num2) / 2);
const ddd = (voz - num1);
const hhh = (voz - num2);


console.log(`средний возраст:${voz} отличие возраста миты от сз:${ddd} отличие возраста тани от сз:${hhh}`);