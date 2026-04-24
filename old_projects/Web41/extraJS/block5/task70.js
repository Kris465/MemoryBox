function calculateAmoebaGrowth(hours) {
    const results = [];
    for (let i = 3; i <= hours; i += 3) {
        const cells = Math.pow(2, i / 3);
        results.push(`Через ${i} часов: ${cells} клеток`);
    }
    return results;
}

const totalHours = 24;
const growthResults = calculateAmoebaGrowth(totalHours);

growthResults.forEach(result => console.log(result));