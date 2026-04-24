const prompt = require('prompt-sync')();
const days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Субота', 'Воскресенье'];
let day = 0;

do {
    console.log(`Сегодня ${days[day]}`);
    day = (day + 1) % days.length;
} while (prompt('Хотите увидеть следующий день ? y/n ').toLowerCase() == 'y');



