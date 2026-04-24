const prompt = require('prompt-sync')();

function dateToSeconds(year, month, day, hours, minutes, seconds){
    const date = new Date(year, month - 1, day, hours, minutes, seconds);
    
    return Math.floor(date.getTime()/1000);
}

function convertSecondsToTimeFormat(totalSeconds){
    const hours = Math.floor(totalSeconds / 3600);
    const minutes = Math.floor((totalSeconds % 3600)/60);
    const seconds = totalSeconds % 60;

    return `${String(hours).padStart(2,'0')}:${String(minutes).padStart(2, '0')}:${String(seconds).padStart(2, '0')}`;
}

function calculatedateDifference(year1, month1, day1, hours1, minutes1, seconds1, year2, month2, day2, hours2, minutes2, seconds2){
    const date1InSeconds = dateToSeconds(year1, month1, day1, hours1, minutes1, seconds1);
    const date2InSeconds = dateToSeconds(year2, month2, day2, hours2, minutes2 , seconds2);

    const differenceInSeconds = Math.abs(date2InSeconds - date1InSeconds);

    return convertSecondsToTimeFormat(differenceInSeconds);
}

console.log("Введите первую дату:");
const year1 = parseInt(prompt('Год: '),10);
const month1 = parseInt(prompt('Месяц: '),10);
const day1 = parseInt(prompt('День: '),10);
const hours1 = parseInt(prompt('Часы: '),10);
const minutes1 = parseInt(prompt('Минуты: '),10);
const seconds1 = parseInt(prompt('Секунды: '),10);

console.log("Введите первую дату:");
const year2 = parseInt(prompt('Год: '),10);
const month2 = parseInt(prompt('Месяц: '),10);
const day2 = parseInt(prompt('День: '),10);
const hours2 = parseInt(prompt('Часы: '),10);
const minutes2 = parseInt(prompt('Минуты: '),10);
const seconds2 = parseInt(prompt('Секунды: '),10);

const result = calculatedateDifference(year1, month1, day1, hours1, minutes1, seconds1,

    year2, month2, day2, hours2, minutes2, seconds2);

    console.log(`Разница между датами: ${result}`);

