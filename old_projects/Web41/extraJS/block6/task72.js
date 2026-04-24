const scores = [];
const n = parseInt(prompt("Введите количество команд:"), 10);
for (let i = 0; i < n; i++) {
    const score = parseFloat(prompt(`Введите очки команды ${i + 1}:`));
    scores.push(score);
}

let isOrdered = true;
for (let i = 0; i < scores.length - 1; i++) {
    if (scores[i] < scores[i + 1]) {
        isOrdered = false;
        break;
    }
}

if (isOrdered) {
    console.log("Команды перечислены в соответствии с занятыми ими местами.");
} else {
    console.log("Команды не перечислены в соответствии с занятыми ими местами.");
}