console.log("Значения квадратного корня для x = 0.2, 0.3, ..., 0.9");
console.log("---------------------------------------------");

for (let i = 2; i <= 9; i++) {
    const x = i / 10; 
    const result = Math.sqrt(x);
    console.log(`√${x.toFixed(1)} = ${result.toFixed(6)}`);
}