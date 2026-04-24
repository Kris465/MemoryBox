const t = 2; 

console.log("x\t|\ty");
console.log("----------------");

for (let x = 4; x <= 28; x++) {
    const y = 2 * Math.pow(t, 2) + t * x + 5.5;
    console.log(`${x}\t|\t${y.toFixed(3)}`);
}