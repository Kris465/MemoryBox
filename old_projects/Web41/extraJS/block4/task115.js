const prompt = require('prompt-sync')();

function getEasternYearName(year) {
    const animals = [
        "Крыса", "Корова", "Тигр", "Заяц", "Дракон",
        "Змея", "Лошадь", "Овца", "Обезьяна", "Петух",
        "Собака", "Свинья"
    ];
    
    const colors = [
        "Зеленый", "Красный", "Желтый", "Белый", "Черный"
    ];

    const baseYear = 1984;

    const yearDifference = year - baseYear;

    const animalIndex = (yearDifference % 12 + 12) % 12; 

    const colorIndex = Math.floor((yearDifference % 10 + 10) % 10 / 2); 

    return `${animals[animalIndex]}, ${colors[colorIndex]}`;
}

const yearInput1 = 1984;
console.log(`Год ${yearInput1}: ${getEasternYearName(yearInput1)}`);

const yearInput2 = parseInt(prompt("Введите год нашей эры:"), 10);
console.log(`Год ${yearInput2}: ${getEasternYearName(yearInput2)}`);