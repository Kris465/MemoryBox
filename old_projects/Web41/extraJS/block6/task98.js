const prompt = require('prompt-sync')(); 

let deposit = 1000;  
const monthlyRate = 0.02;  
let month = 0;  

let increase;
let monthFor30 = 0;
let currentDeposit = deposit;

while (true) {
  increase = currentDeposit * monthlyRate;
  monthFor30++;
  currentDeposit += increase;
  if (increase > 30) break;
}

let monthFor1200 = 0;
currentDeposit = deposit;

while (currentDeposit <= 1200) {
  currentDeposit *= (1 + monthlyRate);
  monthFor1200++;
}

console.log(`а) Ежемесячное увеличение превысит 30 руб. на ${monthFor30}-м месяце`);
console.log(`б) Вклад превысит 1200 руб. через ${monthFor1200} месяцев`);
console.log(`   (Итоговая сумма: ${currentDeposit.toFixed(2)} руб.)`);