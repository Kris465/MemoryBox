console.log("Значения sin(x) для x = 0.1, 0.2, ..., 1.1");
console.log("-------------------------------------");

for (let i = 1; i <= 11; i++) {
    const x = i * 0.1; // Увеличиваем x на 0.1
    const result = Math.sin(x);
    console.log(`sin(${x.toFixed(1)}) = ${result.toFixed(6)}`);
}