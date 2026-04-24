const prompt = require('prompt-sync')();


function feetToKilometers(feet) {
    const meters = feet * 0.305; 
    const kilometers = meters / 1000; 
    return kilometers;
}


function compareDistances(kilometers, feet) {
    const feetInKilometers = feetToKilometers(feet); 

   
    const difference = Math.abs(kilometers - feetInKilometers);

    if (kilometers < feetInKilometers) {
        console.log(`Расстояние в километрах (${kilometers} км) меньше, чем расстояние в футах (${feet} футов).`);
    } else if (kilometers > feetInKilometers) {
        console.log(`Расстояние в футах (${feet} футов) меньше, чем расстояние в километрах (${kilometers} км).`);
    } else {
        console.log(`Оба расстояния равны.`);
    }

   
    console.log(`Цифровая разница между расстояниями: ${difference.toFixed(4)} км.`);
}


const kilometers = parseFloat(prompt("Введите расстояние в километрах:"));
const feet = parseFloat(prompt("Введите расстояние в футах:"));


compareDistances(kilometers, feet);