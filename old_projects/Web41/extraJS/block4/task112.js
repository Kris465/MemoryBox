const prompt = require('prompt-sync')();

function getMonthName(monthIndex) {
    const months = [
        "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь",
        "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ];
    return months[monthIndex];
}

const n = parseInt(prompt("Введите количество месяцев с начала 1990 года:"), 10);


if (isNaN(n) || n < 0) {
    console.log("Некорректный ввод. Пожалуйста, введите неотрицательное целое число.");
} else {
    
    const totalMonths = n; 
    const year = Math.floor(totalMonths / 12); 
    const monthIndex = totalMonths % 12; 


    const yearResult = 1990 + year;
    const monthResult = getMonthName(monthIndex);

    console.log(`Дата: ${monthResult} ${yearResult} года (через ${n} месяцев и 2 дня с начала 1990 года).`);
}