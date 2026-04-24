const prompt = require('prompt-sync')();

function calculateDensity(mass, volume) {
    return mass / volume; 
}

function compareDensities(mass1, volume1, mass2, volume2) {
    const density1 = calculateDensity(mass1, volume1); 
    const density2 = calculateDensity(mass2, volume2); 

    console.log(`Плотность первого тела: ${density1.toFixed(4)} кг/м³`);
    console.log(`Плотность второго тела: ${density2.toFixed(4)} кг/м³`);

    if (density1 > density2) {
        console.log("Материал первого тела имеет большую плотность.");
    } else if (density1 < density2) {
        console.log("Материал второго тела имеет большую плотность.");
    } else {
        console.log("Плотности материалов обоих тел равны.");
    }
}

const mass1 = parseFloat(prompt("Введите массу первого тела (в кг):"));
const volume1 = parseFloat(prompt("Введите объем первого тела (в м³):"));
const mass2 = parseFloat(prompt("Введите массу второго тела (в кг):"));
const volume2 = parseFloat(prompt("Введите объем второго тела (в м³):"));

compareDensities(mass1, volume1, mass2, volume2);