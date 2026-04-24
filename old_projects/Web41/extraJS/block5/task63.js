
const areas = [100, 150, 200, 120, 180, 160, 140, 130, 170, 110];
const yields = [25, 30, 20, 28, 22, 27, 24, 26, 29, 21]; 


function calculateTotalWheatAndAverageYield(areas, yields) {
    let totalWheat = 0; 
    let totalArea = 0; 
    let totalYield = 0; 
    for (let i = 0; i < areas.length; i++) {
        const wheatInDistrict = areas[i] * yields[i]; 
        totalWheat += wheatInDistrict; 
        totalArea += areas[i]; 
        totalYield += yields[i]; 
    }

    const averageYield = totalWheat / totalArea; 

    return {
        totalWheat: totalWheat,
        averageYield: averageYield.toFixed(2) 
    };
}


const result = calculateTotalWheatAndAverageYield(areas, yields);


console.log(`Общее количество пшеницы в области: ${result.totalWheat} центнеров`);
console.log(`Средняя урожайность по области: ${result.averageYield} центнеров с гектара`);