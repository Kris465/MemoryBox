const prompt = require('prompt-sync')();

const totalRemovals = 24;

const teamStats = {
    1: { count: 0, totalTime: 0 },
    2: { count: 0, totalTime: 0 }
};

for (let i = 0; i < totalRemovals; i++) {
    const teamNumber = parseInt(prompt(`Введите номер команды для удаления ${i + 1} (1 или 2):`), 10);
    const duration = parseInt(prompt(`Введите длительность удаления (2, 5 или 10 минут):`), 10);

    if ((teamNumber === 1 || teamNumber === 2) && [2,5,10].includes(duration)) {

        teamStats[teamNumber].count += 1;
        teamStats[teamNumber].totalTime += duration;
    } else {
        alert("Некорректный ввод. Попробуйте снова.");
        i--; 
    }
}

console.log(`Команда 1: всего удалений - ${teamStats[1].count}, общее время - ${teamStats[1].totalTime} минут`);
console.log(`Команда 2: всего удалений - ${teamStats[2].count}, общее время - ${teamStats[2].totalTime} минут`);