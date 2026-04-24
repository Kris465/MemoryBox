const prompt = require('prompt-sync')();

function calculateDistanceAndPath(steps) {
    let distanceFromHome = 0; 
    let totalPath = 0; 

    for (let n = 1; n <= steps; n++) {
        let stepDistance = 1 / n; 

        
        if (n % 2 !== 0) {
            distanceFromHome += stepDistance; 
        } else {
            distanceFromHome -= stepDistance; 
        }

        totalPath += stepDistance; 
    }

    return {
        distanceFromHome: distanceFromHome,
        totalPath: totalPath
    };
}


const steps = 100;
const result = calculateDistanceAndPath(steps);
console.log(`Расстояние от дома после ${steps} этапов: ${result.distanceFromHome.toFixed(6)} км`);
console.log(`Общий путь, пройденный мужчиной: ${result.totalPath.toFixed(6)} км`);