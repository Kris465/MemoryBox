const prompt = require('prompt-sync')(); 

function calculateDistance(V1, V2, S, t) {

    const timeInHours = t / 60; 
    const distance = S + (V1 - V2) * timeInHours; 
    return distance;
}


const V1 = Number(prompt('скорость первого авто: '));
const V2 = Number(prompt('скорость второго авто: '));
const S = 10;
const t = 30;

const distance = calculateDistance(V1, V2, S, t);
console.log(`Расстояние между автомобилями через ${t} минут: ${distance} км`);