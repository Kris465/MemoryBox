const prompt = require('prompt-sync')(); 

class Car {
    constructor(manufacturer, model, year, averageSpeed) {
        this.manufacturer = manufacturer;
        this.model = model;
        this.year = year;
        this.averageSpeed = averageSpeed;
    }

    displayInfo() {
        return `Автомобиль: ${this.manufacturer} ${this.model}, Год выпуска: ${this.year}, Средняя скорость: ${this.averageSpeed} км/ч`;
    }

    calculateTravelTime(distance) {
        const drivingTime = distance / this.averageSpeed;
        const breaks = Math.floor(drivingTime / 4);
        const totalTime = drivingTime + breaks;
        return totalTime;
    }
}

const myCar = new Car('Toyota', 'Camry', 2020, 100);
console.log(myCar.displayInfo()); 

const distance = prompt('Введите расстояние: ');
const travelTime = myCar.calculateTravelTime(distance);
console.log(`Необходимое время для преодоления ${distance} км: ${travelTime.toFixed(2)} часов`); 