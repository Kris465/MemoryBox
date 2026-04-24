const prompt = require('prompt-sync')();

const populations = [50, 80, 120, 60, 90, 110, 70, 40, 30, 100, 150, 200];
const densities = [500, 400, 800, 500, 600, 700, 300, 200, 150, 900, 1000, 1200];

function calculateTotalArea(populations, densities) {
    let totalArea = 0;

    for (let i = 0; i < populations.length; i++) {
        const area = populations[i] / densities[i];
        totalArea += area;
    }

    return totalArea;
}

const totalArea = calculateTotalArea(populations, densities);
console.log(`Общая площадь территории области: ${totalArea.toFixed(2)} км²`);