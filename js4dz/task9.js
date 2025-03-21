const prompt = require('prompt-sync')();

// Функция для преобразования секунд в формат "чч:мм:сс"
function convertSecondsToTimeFormat(totalSeconds) {
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600) / 60);
    const seconds = totalSeconds % 60;

    // Форматируем часы, минуты и секунды с ведущими нулями
    const formattedTime = `${String(hours).padStart(2, '0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
    return formattedTime;
}

// Получаем ввод от пользователя
const secondsInput = prompt('Введите количество секунд: ');

// Преобразуем ввод в число
const totalSeconds = parseInt(secondsInput, 10);

// Вычисляем время в формате "чч:мм:сс"
const formattedTime = convertSecondsToTimeFormat(totalSeconds);

// Выводим результат
console.log(`Время в формате "чч:мм:сс": ${formattedTime}`);
