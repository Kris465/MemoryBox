const prompt = require('prompt-sync')();

// Функция для преобразования времени в секунды
function convertToSeconds(hours, minutes, seconds) {
    return (hours * 3600) + (minutes * 60) + seconds;
}

// Получаем ввод от пользователя
const hoursInput = prompt('Введите часы: ');
const minutesInput = prompt('Введите минуты: ');
const secondsInput = prompt('Введите секунды: ');

// Преобразуем ввод в числа
const hours = parseInt(hoursInput, 10);
const minutes = parseInt(minutesInput, 10);
const seconds = parseInt(secondsInput, 10);

// Вычисляем общее количество секунд
const totalSeconds = convertToSeconds(hours, minutes, seconds);

// Выводим результат
console.log(`Общее время в секундах: ${totalSeconds}`);
