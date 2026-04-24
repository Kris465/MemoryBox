const prompt = require('prompt-sync')();

function totalResistance(resistances) {
    if (resistances.length === 0) {
        return 0; 
    }

    const reciprocalSum = resistances.reduce((accumulator, current) => accumulator + (1 / current), 0);
    
    const totalR = 1 / reciprocalSum;
    
    return totalR;
}

const resistances = [10, 20, 30]; 

const result = totalResistance(resistances);
console.log(`Общее сопротивление цепи: ${result.toFixed(2)} Ом`); 