const prompt = require('prompt-sync')();

function kmhToMps(kmh) {
    return kmh / 3.6; 
}

function compareSpeeds(kmh, mps) {
    const mpsFromKmh = kmhToMps(kmh); 

    if (mpsFromKmh > mps) {
        console.log(`Скорость в километрах в час (${kmh} км/ч) больше, чем скорость в метрах в секунду (${mps} м/с).`);
    } else if (mpsFromKmh < mps) {
        console.log(`Скорость в метрах в секунду (${mps} м/с) больше, чем скорость в километрах в час (${kmh} км/ч).`);
    } else {
        console.log(`Обе скорости равны.`);
    }
}

const kmh = parseFloat(prompt("Введите скорость в километрах в час (км/ч):"));
const mps = parseFloat(prompt("Введите скорость в метрах в секунду (м/с):"));

compareSpeeds(kmh, mps);