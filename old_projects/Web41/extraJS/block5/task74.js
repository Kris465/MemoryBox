function calculateTotalVolume(innerDiameter, wallThickness, numberOfBalls) {
    const totalVolume = [];
    let currentDiameter = innerDiameter;

    for (let i = 0; i < numberOfBalls; i++) {
        const radius = (currentDiameter / 2) / 100; 
        const volume = (4 / 3) * Math.PI * Math.pow(radius, 3); 
        totalVolume.push(volume);
        currentDiameter += wallThickness * 2; 
    }

    return totalVolume.reduce((sum, volume) => sum + volume, 0) * 1000; 
}

const innerDiameter = 10; 
const wallThickness = 0.5; 
const numberOfBalls = 12;

const totalVolumeInLiters = calculateTotalVolume(innerDiameter, wallThickness, numberOfBalls);
console.log(`Суммарный объем двенадцати вложенных шаров: ${totalVolumeInLiters.toFixed(2)} литров`);