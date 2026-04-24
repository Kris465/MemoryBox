const prompt = require('prompt-sync')();



class Time {
    constructor(hours, minutes, seconds) {
        
        if (hours < 0 || hours > 23 || minutes < 0 || minutes > 59 || seconds < 0 || seconds > 59) {
            throw new Error("Некорректное время. Часы должны быть от 0 до 23, минуты и секунды — от 0 до 59.");
        }
        this.hours = hours;
        this.minutes = minutes;
        this.seconds = seconds;
        
    }

  
    display() {
        const format = (value) => String(value).padStart(2, '0'); 
        return `${format(this.hours)}:${format(this.minutes)}:${format(this.seconds)}`;
    }

    
    addSeconds(seconds) {
        this.seconds += seconds;
        this.normalizeTime();
    }

    addMinutes(minutes) {
        this.minutes += minutes;
        this.normalizeTime();
    }

    addHours(hours) {
        this.hours += hours;
        this.normalizeTime();
    }

    normalizeTime() {
        let extraMinutes = Math.floor(this.seconds / 60);
        this.seconds %= 60;
        this.minutes += extraMinutes;

        let extraHours = Math.floor(this.minutes / 60);
        this.minutes %= 60;
        this.hours += extraHours;

        this.hours %= 24; 
    }
}
const hoursInput = prompt('Введите часы:');
const minutesInput = prompt('Введите минуты:');
const secondsInput = prompt('Введите секунды:');

const time = new Time(hoursInput, minutesInput, secondsInput);
console.log("Начальное время:", time.display()); 

time.addSeconds(30);
console.log("После добавления 30 секунд:", time.display()); 

time.addMinutes(45);
console.log("После добавления 45 минут:", time.display()); 

time.addHours(2);
console.log("После добавления 2 часов:", time.display()); 

time.addSeconds(3600); 
console.log("После добавления 3600 секунд:", time.display()); 