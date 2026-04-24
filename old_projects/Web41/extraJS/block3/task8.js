
let X = false;
let Y = true; 
let Z = false;

let a = X && !(Z || Y) || !Z;
console.log("а) X и не (Z или Y) или не Z:", a); 

let b = !X || (X && (Y || Z));
console.log("б) не X или X и (Y или Z):", b); 

let v = (X || (Y && !Z)) && Z;
console.log("в) (X или Y и не Z) и Z:", v); 