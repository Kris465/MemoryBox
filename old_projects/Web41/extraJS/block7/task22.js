const prompt = require('prompt-sync')();

let totalMagazinePages = 0;
while (true) {
    const input = prompt("Введите количество страниц в журнале (или пустая строка для завершения):");
    if (input === null || input.trim() === "") {
        break;
    }
    const pages = parseInt(input, 10);
    if (!isNaN(pages)) {
        totalMagazinePages += pages;
    } else {
        console.log("Некорректный ввод");
    }
}
console.log("Общее число страниц во всех журналах:", totalMagazinePages);