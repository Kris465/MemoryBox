
let X = false; 
let Y = false; 
let Z = true; 

let a = X || (Y && !Z);
console.log("а) X или Y и не Z:", a); 

let g = (X && !Y) || Z;
console.log("г) X и не Y или Z:", g); 

let b = !X && !Y;
console.log("б) не X и не Y:", b);

let v = ! (X && Z) || Y;
console.log("в) не (X и Z) или Y:", v); 

let d = X && (!Y || Z);
console.log("д) X и (не Y или Z):", d);

let e = X || !(Y || Z);
console.log("е) X или (не (Y или Z)):", e);