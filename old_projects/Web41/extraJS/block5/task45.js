const prompt = require('prompt-sync')();

function totalResistance(resistances) {
    const totalR = resistances.reduce((accumulator, current) => accumulator + current, 0);
    return totalR;
}

const resistances = [10, 20, 30, 5];

const result = totalResistance(resistances);
console.log(`Общее сопротивление цепи: ${result} Ом`);