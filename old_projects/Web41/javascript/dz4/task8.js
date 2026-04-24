const prompt = require('prompt-sync')();

function convertToSeconds(hours, minutes, seconds){
    return(hours * 3600) + (minutes * 60) + seconds;
}

const hoursInput = prompt('Введите часы:');
const minutesInput = prompt('Введите минуты:');
const secondsInput = prompt('Введите секунды:');

const hours = parseInt(hoursInput,10);
const minutes = parseInt(minutesInput,10);
const seconds = parseInt(secondsInput,10);

const totalSeconds = convertToSeconds(hours,minutes,seconds);

console.log(`Общее время в секундах: ${totalSeconds}`);