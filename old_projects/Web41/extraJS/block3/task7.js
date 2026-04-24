let A = true;  
let B = false; 
let C = false; 

let a = A || !(A && B) || C;
console.log("а) A или не (A и B) или C:", a); 
let b = !A || (A && (B || C));
console.log("б) не A или A и (B или C):", b); 
let v = (A || (B && !C)) && C;
console.log("в) (A или B и не C) и C:", v);