class Vehicle {
    constructor(manufacturer, model, year, averageSpeed) {
    this.manufacturer = manufacturer;
    this.model = model;
    this.year = year;
    this.averageSpeed = averageSpeed;
    }
    displayInfo() {
        console.log(`Производитель: ${this.manufacturer}`);
        console.log(`Модель: ${this.model}`);
        console.log(`Год выпуска: ${this.year}`);
        console.log(`Средняя скорость: ${this.averageSpeed} км/ч`);
    }
}

class Car extends Vehicle {
    constructor(manufacturer,model,year,averageSpeed) {
        super(manufacturer, model, year, averageSpeed)
    }

    calculateTravelTime(distance) {
        let travelTime = distance / this.averageSpeed;
        const breaks = Math.floor(travelTime / 4);
        const totalTravelTime = travelTime + breaks;

        return totalTravelTime;
    }
}

const myCar = new Car('Toyota', 'Camry', 2020,100);
myCar.displayInfo();

const distance = 500;
const travelTime = myCar.calculateTravelTime(distance);
console.log(`Время в пути на расстояние ${distance} км: ${travelTime.toFixed(2)}часов`)