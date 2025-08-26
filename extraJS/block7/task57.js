const prompt = require('prompt-sync')();

// Ввод данных
const speeds = [];
const totalCars = 20;

for (let i = 0; i < totalCars; i++) {
    const speed = parseFloat(prompt(`Введите максимальную скорость автомобиля марки ${i + 1}:`));
    speeds.push(speed);
}

// Находим максимальную скорость
let maxSpeed = speeds[0];

for (let i = 1; i < totalCars; i++) {
    if (speeds[i] > maxSpeed) {
        maxSpeed = speeds[i];
    }
}

// Вывод результата
console.log(`Максимальная скорость самого быстрого автомобиля: ${maxSpeed}`);