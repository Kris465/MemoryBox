const prompt = require('prompt-sync')(); 

function convertTemperature(celsius) {

    const fahrenheit = Math.round((celsius * 1.8 + 32) * 10) / 10; 


    const kelvin = Math.round(celsius + 273.15);

    return {
        fahrenheit: fahrenheit,
        kelvin: kelvin
    };
}

const celsiusTemperature = Number(prompt('Введите температуру в C*: '));; 
const convertedTemperatures = convertTemperature(celsiusTemperature);

console.log(`Температура по шкале Фаренгейта: ${convertedTemperatures.fahrenheit} °F`);
console.log(`Температура по шкале Кельвина: ${convertedTemperatures.kelvin} K`);