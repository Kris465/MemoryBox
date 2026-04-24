const prompt = require('prompt-sync')();


function timePassedInSeconds(n) {

    const hours = Math.floor(n / 3600);
    
    const secondsAfterHours = n % 3600;
    
    const minutes = Math.floor(secondsAfterHours / 60);
    
    const seconds = secondsAfterHours % 60;
    
    return {
        hours: hours,
        minutes: minutes,
        seconds: seconds
    };
}

const n = Number(prompt("Введите колличество секунд : "));
const result = timePassedInSeconds(n);

console.log(`Полные часы: ${result.hours}`);
console.log(`Полные минуты: ${result.minutes}`);
console.log(`Полные секунды: ${result.seconds}`);