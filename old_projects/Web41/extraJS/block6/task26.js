const prompt = require('prompt-sync')();

let prevNumber = null;
let signChanges = 0;

while (true) {
    const num = parseInt(prompt("Введите число (0 для завершения):"));
    if (num === 0) break;
    if (prevNumber !== null && prevNumber * num < 0) {
        signChanges++;
    }
    prevNumber = num;
}

console.log("Количество изменений знака: " + signChanges);