const p0 = 1.29; 
const z = 1250; 

console.log("Высота (м)\tПлотность (кг/м³)");
for (let h = 0; h <= 1000; h += 100) {
    const p = p0 * Math.exp(-h / z);
    console.log(`${h}\t\t${p.toFixed(3)}`);
}