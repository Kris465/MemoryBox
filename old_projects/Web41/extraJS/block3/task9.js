
let X = true;  
let Y = false;  
let Z = false;  


let a = !X || !Y || !Z;
console.log("а) не X или не Y или не Z:", a); 

let b = (!X || !Y) && (X || Y);
console.log("б) (не X или не Y) и (X или Y):", b); 

let v = (X && Y) || (X && Z) || !Z;
console.log("в) X и Y или X и Z или не Z:", v); 