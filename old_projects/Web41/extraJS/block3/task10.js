
let A = false; 
let B = false; 
let C = true;  


let a = (!A || !B) && !C;
console.log("а) (не A или не B) и не C:", a); 


let b = (!A || !B) && (A || B);
console.log("б) (не A или не B) и (A или B):", b); 


let v = (A && B) || (A && C) || !C;
console.log("в) A и B или A и C или не C:", v); 