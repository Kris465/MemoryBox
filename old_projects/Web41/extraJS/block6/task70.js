const prompt = require('prompt-sync')(); 

const sequence = [];
while (true) {
    const input = prompt("Введите число (или 10000 для завершения):");
    const num = parseFloat(input);
    if (isNaN(num)) continue;
    sequence.push(num);
    if (num === 10000) break;
}

let violationIndex = -1;
for (let i = 0; i < sequence.length - 1; i++) {
    if (sequence[i] > sequence[i + 1]) {
        violationIndex = i + 1;
        break;
    }
}

if (violationIndex === -1) {
    console.log("Последовательность упорядочена по возрастанию.");
} else {
    console.log(`Последовательность не упорядочена. Нарушение в позиции ${violationIndex}.`);
}