const prompt = require('prompt-sync')(); 

let dailyDistance = 10; 
let totalDistance = dailyDistance;
let dayCount = 1; 

let dayOver20 = 0;
let currentDaily = dailyDistance;

while (currentDaily <= 20) {
  currentDaily *= 1.1; 
  dayOver20++;
}

let dayOver100 = 1;
currentDaily = dailyDistance;
totalDistance = currentDaily;

while (totalDistance <= 100) {
  currentDaily *= 1.1;
  totalDistance += currentDaily;
  dayOver100++;
}

console.log(`а) Лыжник пробежит больше 20 км на ${dayOver20}-й день`);
console.log(`   (В этот день он пробежит ${currentDaily.toFixed(2)} км)`);
console.log(`б) Суммарный пробег превысит 100 км на ${dayOver100}-й день`);
console.log(`   (Общий пробег: ${totalDistance.toFixed(2)} км)`);