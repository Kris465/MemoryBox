function calculateSkiRun(initialDistance, dailyIncreaseRate, totalDays) {
    const dailyDistances = [];
    let currentDistance = initialDistance;

    for (let day = 1; day <= totalDays; day++) {
        dailyDistances.push(currentDistance);
        currentDistance += currentDistance * (dailyIncreaseRate / 100);
    }

    return dailyDistances;
}

function calculateTotalDistance(dailyDistances) {
    return dailyDistances.reduce((total, distance) => total + distance, 0);
}

const initialDistance = 10;
const dailyIncreaseRate = 10; 
const totalDays = 10;

const dailyDistances = calculateSkiRun(initialDistance, dailyIncreaseRate, totalDays);

console.log("Пробег лыжника за второй, третий, ..., десятый день:");
for (let i = 1; i < totalDays; i++) {
    console.log(`День ${i + 1}: ${dailyDistances[i].toFixed(2)} км`);
}

const totalDistanceIn7Days = calculateTotalDistance(dailyDistances.slice(0, 7));
console.log(`\nСуммарный путь за первые 7 дней тренировок: ${totalDistanceIn7Days.toFixed(2)} км`);