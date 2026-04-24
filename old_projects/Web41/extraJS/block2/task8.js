const prompt = require('prompt-sync')();

function dayOfWeek(k, d) {
    const startOffset = (d - 1) % 7;
    const dayNumber = (startOffset + (k - 1)) % 7;
    return dayNumber;
}

const k = 10; 
const d1 = 1; 
const d2 = 2; 
const d3 = 3;

console.log(`Для 1 января - понедельник (k = ${k}):`, dayOfWeek(k, d1)); 
console.log(`Для 1 января - вторник (k = ${k}):`, dayOfWeek(k, d2));    
console.log(`Для 1 января - среда (k = ${k}):`, dayOfWeek(k, d3));  