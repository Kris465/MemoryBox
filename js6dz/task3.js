class Time {
    constructor(hours, minutes, seconds) {
        this.hours = hours;
        this.minutes = minutes;
        this.seconds = seconds;
        this.normalize();
    }
    normalize() {
        if (this.seconds >= 60) {
            this.minutes += Math.floor(this.seconds / 60);
            this.seconds = this.seconds % 60;
        } else if (this.seconds < 0) {
            const minutesToSubtract = Math.ceil(Math.abs(this.seconds) / 60);
            this.minutes -= minutesToSubtract;
            this.seconds = (this.seconds + 60 * minutesToSubtract) % 60;
        }

        if (this.minutes >= 60) {
            this.hours += Math.floor(this.minutes / 60);
            this.minutes = this.minutes % 60;
        } else if (this.minutes < 0) {
            const hoursToSubtract = Math.ceil(Math.abs(this.minutes) / 60);
            this.hours -= hoursToSubtract;
            this.minutes = (this.minutes + 60 * hoursToSubtract) % 60;
        }
        this.hours = (this.hours + 24) % 24; 
    }
    displayTime() {
        return `${this.pad(this.hours)}:${this.pad(this.minutes)}:${this.pad(this.seconds)}`;
    }
    addSeconds(seconds) {
        this.seconds += seconds;
        this.normalize();
    }
    addMinutes(minutes) {
        this.minutes += minutes;
        this.normalize();
    }
    addHours(hours) {
        this.hours += hours;
        this.normalize();
    }
    pad(number) {
        return number < 10 ? '0' + number : number;
    }
}

const time = new Time(20, 30, 45);

console.log(`Текущее время: ${time.displayTime()}`);

time.addSeconds(30);
console.log(`После добавления 30 секунд: ${time.displayTime()}`);

time.addMinutes(5);
console.log(`После добавления 5 минут: ${time.displayTime()}`);

time.addHours(3);
console.log(`После добавления 3 часов: ${time.displayTime()}`);

time.addMinutes(-100);
console.log(`После убирания 100 минут: ${time.displayTime()}`);
