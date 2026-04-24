const prompt = require('prompt-sync')();

const rasst = prompt("введите расстояние в сантиметрах: ");

function getFullMeters(cm) {
    return Math.floor(cm / 100);
}

let fullMeters = getFullMeters(rasst);
console.log(`${fullMeters}`)