let A, B, C;
let conditionA = (A > 100) && (B > 100);
let conditionB = (A % 2 === 0) !== (B % 2 === 0);
let conditionC = (A > 0) || (B > 0);
let conditionD = (A % 3 === 0) && (B % 3 === 0) && (C % 3 === 0);
let conditionE = (A < 50) + (B < 50) + (C < 50) === 1;
let conditionF = (A < 0) || (B < 0) || (C < 0);
A = 120; 
B = 102; 
C = 30; 

console.log(`Условие A: ${conditionA}`); 
console.log(`Условие B: ${conditionB}`); 
console.log(`Условие C: ${conditionC}`); 
console.log(`Условие D: ${conditionD}`); 
console.log(`Условие E: ${conditionE}`); 
console.log(`Условие F: ${conditionF}`); 