const prompt = require('prompt-sync')();

const teamA = { removals: 0, penaltyTime: 0 };
const teamB = { removals: 0, penaltyTime: 0 };

while (true) {
    const inputA = prompt("Введите время удаления для команды А (2, 5, 10 или 0 для завершения):");
    const timeA = parseInt(inputA);
    if (timeA === 0) break;
    if ([2, 5, 10].includes(timeA)) {
        teamA.removals++;
        teamA.penaltyTime += timeA;
    } else {
        alert("Некорректный ввод. Повторите.");
        continue;
    }

    const inputB = prompt("Введите время удаления для команды Б (2, 5, 10 или 0 для завершения):");
    const timeB = parseInt(inputB);
    if (timeB === 0) break;
    if ([2, 5, 10].includes(timeB)) {
        teamB.removals++;
        teamB.penaltyTime += timeB;
    } else {
        alert("Некорректный ввод. Повторите.");
        continue;
    }
}

console.log(`Команда А: всего удалений - ${teamA.removals}, штрафное время - ${teamA.penaltyTime} минут`);
console.log(`Команда Б: всего удалений - ${teamB.removals}, штрафное время - ${teamB.penaltyTime} минут`);