const prompt = require('prompt-sync')();

const januaryPrecipitation = [2.5, 0, 1.2, 3.0, 0, 0, 4.1, 2.3, 0, 1.5, 
    0, 0, 2.7, 1.8, 0, 3.3, 0, 2.4, 1.1, 
    0, 0]; 

const marchPrecipitation = [1.5, 2.0, 0, 3.5, 4.2, 
 1.8, 0, 2.9, 3.1, 
 0, 1.7, 2.6, 0,
 4.5, 3.3]; 

function calculateAverage(precipitation) {
const total = precipitation.reduce((accumulatedSum, current) => accumulatedSum + current, 0);
return total / precipitation.length;
}

const averageJanuary = calculateAverage(januaryPrecipitation);
const averageMarch = calculateAverage(marchPrecipitation);

console.log(`Среднедневное количество осадков за январь: ${averageJanuary.toFixed(2)} мм`);
console.log(`Среднедневное количество осадков за март: ${averageMarch.toFixed(2)} мм`);