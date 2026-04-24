const prompt = require('prompt-sync')();

function calculateYieldAndArea(initialArea, initialYield, areaIncreaseRate, yieldIncreaseRate, totalYears) {
    const yields = [];
    const areas = [];
    let currentArea = initialArea;
    let currentYield = initialYield;

    for (let year = 1; year <= totalYears; year++) {
        if (year > 1) {
            currentYield *= (1 + yieldIncreaseRate / 100);
            yields.push(currentYield);
        } else {
            yields.push(currentYield);
        }
        
        currentArea *= (1 + areaIncreaseRate / 100);
        areas.push(currentArea);
    }

    return { yields, areas };
}

function calculateTotalHarvest(yields, areas) {
    let totalHarvest = 0;
    for (let i = 0; i < yields.length; i++) {
        totalHarvest += yields[i] * areas[i];
    }
    return totalHarvest;
}

const initialArea = 100;
const initialYield = 20; 
const areaIncreaseRate = 5; 
const yieldIncreaseRate = 2; 
const totalYears = 8;

const { yields, areas } = calculateYieldAndArea(initialArea, initialYield, areaIncreaseRate, yieldIncreaseRate, totalYears);

console.log("Урожайность за второй, третий, ..., восьмой год:");
for (let i = 1; i < yields.length; i++) {
    console.log(`Год ${i + 1}: ${yields[i].toFixed(2)} центнеров с гектара`);
}

console.log("\nПлощадь участка в четвертый, пятый, ..., седьмой год:");
for (let i = 3; i < areas.length; i++) {
    console.log(`Год ${i + 1}: ${areas[i].toFixed(2)} гектаров`);
}

const totalHarvestInSixYears = calculateTotalHarvest(yields.slice(0, 6), areas.slice(0, 6));
console.log(`\nУрожай за первые шесть лет: ${totalHarvestInSixYears.toFixed(2)} центнеров`);