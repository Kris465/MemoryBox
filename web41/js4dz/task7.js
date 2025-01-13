const prompt = require('prompt-sync')();

// Функция для форматирования времени
function formatTime(hours, minutes = 0, seconds = 0) {
    // Приводим часы, минуты и секунды к строковому формату с ведущими нулями
    const formattedHours = String(hours).padStart(2, '0');
    const formattedMinutes = String(minutes).padStart(2, '0');
    const formattedSeconds = String(seconds).padStart(2, '0');

    // Возвращаем отформатированное время
    return `${formattedHours}:${formattedMinutes}:${formattedSeconds}`;
}

// Получаем ввод от пользователя
const hoursInput = prompt('Введите часы: ');
const minutesInput = prompt('Введите минуты (по умолчанию 00): ');
const secondsInput = prompt('Введите секунды (по умолчанию 00): ');

// Преобразуем ввод в числа
const hours = parseInt(hoursInput, 10);
const minutes = minutesInput ? parseInt(minutesInput, 10) : 0; // Если минуты не введены, устанавливаем 0
const seconds = secondsInput ? parseInt(secondsInput, 10) : 0; // Если секунды не введены, устанавливаем 0

// Выводим отформатированное время
const formattedTime = formatTime(hours, minutes, seconds);
console.log(`Отформатированное время: ${formattedTime}`);
