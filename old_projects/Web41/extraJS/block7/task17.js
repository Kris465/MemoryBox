const m = 5; 
const n = 3; 
const x = [4, 9, -6, 7, 12]; 

const sum = x.reduce((acc, num) => (num % n === 0 ? acc + num : acc), 0);
console.log(sum);