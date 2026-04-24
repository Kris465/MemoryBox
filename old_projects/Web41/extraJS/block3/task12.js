
let x1 = 1; 
let y1 = 1; 

let x2 = 2; 
let y2 = 1; 


let a = (2 * 2 < 0) && (x1 < y1);
console.log("а) 2 * 2 < 0 && x < y:", a); 


let b = (x2 > 2) || (2 < (4 && y2));
console.log("б) (x > 2) || (2 < (4 && y)):", b); 


let v = (x2 > 0) && (2 < (4 && y2));
console.log("в) (x > 0) && (2 < (4 && y)):", v); 


let g = (x2 * y2 == 4) && (y2 > x2);
console.log("г) (x * y == 4) && (y > x):", g); 


let d = (x1 * y1 == 0) || (y1 < x1);
console.log("д) (x * y == 0) || (y < x):", d); 


let e = !(x2 * y2 < 1) && (y2 > x2);
console.log("е) !(x * y < 1) && (y > x):", e); 


let j = !(x1 * y1 < 0) || (y1 > x1);
console.log("ж) !(x * y < 0) || (y > x):", j); 