
const populations = [50, 80, 120, 60, 90, 110, 70, 40, 30, 100, 150, 200]; 
const areas = [100, 200, 150, 120, 180, 160, 140, 130, 170, 110, 90, 80]; 


function calculateAveragePopulationDensity(populations, areas) {
    let totalPopulation = 0; 
    let totalArea = 0; 

    for (let i = 0; i < populations.length; i++) {
        totalPopulation += populations[i]; 
        totalArea += areas[i]; 
    }

    const averageDensity = totalPopulation / totalArea; 

    return averageDensity.toFixed(2); 
}


const averageDensity = calculateAveragePopulationDensity(populations, areas);


console.log(`Средняя плотность населения по области: ${averageDensity} тысяч человек на км²`);