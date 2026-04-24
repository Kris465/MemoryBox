const prompt = require('prompt-sync')();

function calculateAverage(masses) {
    const sum = masses.reduce((accumulator, current) => accumulator + current, 0);
    return sum / masses.length;
}

function getMassesFromUser() {
    const readline = require('readline');
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Введите массы предметов через запятую: ', (input) => {
        const masses = input.split(',').map(Number);
        if (masses.length === 0 || masses.some(isNaN)) {
            console.log("Пожалуйста, введите корректные массы.");
        } else {
            const result = calculateAverage(masses);
            console.log(`Средняя масса предметов: ${result}`);
        }
        rl.close();
    });
}

getMassesFromUser();