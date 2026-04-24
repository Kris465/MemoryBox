const R = 6350; 

console.log("Высота (км)\tРасстояние до горизонта (км)");
for (let h = 1; h <= 10; h++) {
    const d = Math.sqrt((R + h) ** 2 - R ** 2);
    console.log(`${h}\t\t${d.toFixed(3)}`);
}