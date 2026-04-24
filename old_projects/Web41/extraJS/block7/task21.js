const prompt = require('prompt-sync')();

let totalCost = 0;
while (true) {
    const input = prompt("Введите стоимость товара (или пустая строка для завершения):");
    if (input === null || input.trim() === "") {
        break;
    }
    const cost = parseFloat(input);
    if (!isNaN(cost)) {
        if (cost > 1000) {
            totalCost += cost;
        }
    } else {
        console.log("Некорректный ввод");
    }
}
console.log("Общая стоимость товаров дороже 1000 рублей:", totalCost);