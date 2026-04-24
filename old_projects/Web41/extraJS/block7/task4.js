let a = 1; 
let b = 100; 
let sum = 0;

for (let i = a; i <= b; i++) {
  if (i % 4 === 0 && i > 0) {
    sum += i;
  }
}

console.log(sum);