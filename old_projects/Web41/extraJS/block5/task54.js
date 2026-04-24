const prompt = require('prompt-sync')();

function calculateAverage(grades) {
    const sum = grades.reduce((accumulator, current) => accumulator + current, 0);
    const average = sum / grades.length;
    return average;
}

function getGradesFromUser() {
    const readline = require('readline');

    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Введите оценки по алгебре для учеников через запятую (например: 5,4,3,2,...): ', (input) => {

        const grades = input.split(',').map(Number);

        if (grades.length === 0 || grades.some(isNaN)) {
            console.log("Пожалуйста, введите корректные оценки.");
        } else {
            const result = calculateAverage(grades);
            console.log(`Средняя оценка по алгебре: ${result}`);
        }

        rl.close();
    });
}

getGradesFromUser();