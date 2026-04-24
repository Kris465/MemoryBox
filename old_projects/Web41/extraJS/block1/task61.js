const prompt = require('prompt-sync')();

let a = prompt("Введите первое значение (a): ");

function calculatePowers(a){
    let a1 = a * a; 
    let a0 = a1 * a1; 
    console.log(`a^4 = ${a0}`)

    let a2 = a * a;  
    let a6 = a2 * a2 * a2; 
    console.log(`a^6 = ${a6}`);

    
    let a7 = a6 * a;   
    console.log(`a^7 = ${a7}`);

    
    let a4 = a2 * a2;    
    let a8 = a4 * a4;    
    console.log(`a^8 = ${a8}`);

    
    let a9 = a8 * a;     
    console.log(`a^9 = ${a9}`);

   
    let a5 = a2 * a2 * a; 
    let a10 = a5 * a5;   
    console.log(`a^10 = ${a10}`);
}


let result = calculatePowers(a);
console.log(result); 