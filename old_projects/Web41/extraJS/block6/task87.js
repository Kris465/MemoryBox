const prompt = require('prompt-sync')(); 

let score1 = 0;
let score2 = 0;

while (true) {
    const input = prompt("Введите очки, набранные командой (1, 2 или 3). Для завершения игры введите 0:");
    const points = parseInt(input, 10);

    if (points === 0) {
        break;
    }

    if (points === 1 || points === 2 || points === 3) {
        const teamNumber = prompt("Введите номер команды (1 или 2):");
        if (teamNumber === '1') {
            score1 += points;
        } else if (teamNumber === '2') {
            score2 += points;
        } else {
           console.log("Некорректный номер команды. Попробуйте снова.");
            continue;
        }
        console.log(`Текущий счет: команда 1 - ${score1}, команда 2 - ${score2}`);
    } else {
        console.log("Некорректное количество очков. Введите 1, 2 или 3.");
    }
}

let resultMessage = "";
if (score1 > score2) {
    resultMessage = "Игра окончена. Победила команда 1.";
} else if (score2 > score1) {
    resultMessage = "Игра окончена. Победила команда 2.";
} else {
    resultMessage = "Игра окончена. Ничья.";
}

console.log(`Итоговый счет: команда 1 - ${score1}, команда 2 - ${score2}.\n${resultMessage}`);