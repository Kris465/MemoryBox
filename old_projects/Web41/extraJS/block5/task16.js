console.log("Значения sin(x) для x = 2, 3, ..., 20");
console.log("-------------------------------------");

for (let i = 2; i <= 20; i++) {
    const result = Math.sin(i);
    console.log(`sin(${i}) = ${result.toFixed(6)}`);
}