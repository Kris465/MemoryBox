const prompt = require('prompt-sync')();

const daysOfWeek = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'];
let currentDayIndex = 0;

do {
    console.log(daysOfWeek[currentDayIndex]);
    currentDayIndex = (currentDayIndex + 1) % daysOfWeek.length;
} while (prompt('Хотите увидеть следующий день? (y/n): ').toLowerCase() === 'y');
