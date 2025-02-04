const prompt = require('prompt-sync')(); 

class Time {
    constructor(hours, minutes, seconds) {
        this.hours = hours;
        this.minutes = minutes;
        this.seconds = seconds;
        this.normalizeTime();
    }

    normalizeTime() {
        if (this.seconds >= 60) {
            this.minutes += Math.floor(this.seconds / 60);
            this.seconds = this.seconds % 60;
        } else if (this.seconds < 0) {
            this.minutes -= Math.ceil(Math.abs(this.seconds) / 60);
            this.seconds = (this.seconds % 60 + 60) % 60;
        }

        if (this.minutes >= 60) {
            this.hours += Math.floor(this.minutes / 60);
            this.minutes = this.minutes % 60;
        } else if (this.minutes < 0) {
            this.hours -= Math.ceil(Math.abs(this.minutes) / 60);
            this.minutes = (this.minutes % 60 + 60) % 60;
        }
        this.hours = (this.hours % 24 + 24) % 24; 
    }

    displayTime() {
        return `${String(this.hours).padStart(2, '0')}:${String(this.minutes).padStart(2, '0')}:${String(this.seconds).padStart(2, '0')}`;
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
}

const time = new Time(20, 30, 45);
console.log(time.displayTime()); 

time.addSeconds(30);
console.log(time.displayTime());

time.addMinutes(5);
console.log(time.displayTime()); 

time.addHours(3);
console.log(time.displayTime());

time.addHours(1);
console.log(time.displayTime()); 