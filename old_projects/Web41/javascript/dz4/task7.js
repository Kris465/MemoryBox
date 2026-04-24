const prompt = require('prompt-sync')();
function formatTime(hours, minutes = 0, sconds = 0) {
    const formattedHours = 
    String(hours).padStart(2, '0');

    const formattedMinutes = 
    String(minutes).padStart(2, '0');

    const formattedSeconds = 
    String(seconds).padStart(2, '0');

    return `${formattedHours}:${formattedMinutes}:${formattedSeconds}`;

}

const hoursInput = prompt('Введите часы: ');
const minutesInput = prompt('Введите минуты(по умолчанию 00): ');
const secondsInput = prompt('Введите секунды (по умолчанию 00): ')

const hours = parseInt(hoursInput, 10);
const minutes = minutesInput ?
parseInt(minutesInput, 10) : 0;
const seconds = secondsInput ?
parseInt(secondsInput, 10) : 0;

const formattedTime = formatTime(hours, minutes, seconds);
console.log(`Отформатированное время: ${formattedTime}`);