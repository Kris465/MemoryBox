const prompt = require('prompt-sync')(); 



let year = 1;
let area = 100; 
let yield = 20; 
let totalHarvest = area * yield;

let yearForYield = 1;
let currentYield = yield;

while (currentYield <= 22) {
  currentYield *= 1.02; 
  yearForYield++;
}


let yearForArea = 1;
let currentArea = area;

while (currentArea <= 120) {
  currentArea *= 1.05; 
  yearForArea++;
}


let yearForTotal = 1;
currentArea = area;
currentYield = yield;
let cumulativeHarvest = currentArea * currentYield;

while (cumulativeHarvest <= 800) {
  yearForTotal++;
  currentArea *= 1.05;
  currentYield *= 1.02;
  cumulativeHarvest += currentArea * currentYield;
}


console.log(`а) Урожайность превысит 22 ц/га в ${yearForYield}-м году (${currentYield.toFixed(2)} ц/га)`);
console.log(`б) Площадь превысит 120 га в ${yearForArea}-м году (${currentArea.toFixed(2)} га)`);
console.log(`в) Общий урожай превысит 800 ц в ${yearForTotal}-м году (${cumulativeHarvest.toFixed(2)} ц)`);