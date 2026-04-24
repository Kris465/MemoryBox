const prompt = require('prompt-sync')();

class Circle {
    constructor(radius) {
        this._radius = radius; 
    }

    get radius() {
        return this._radius;
    }

    set radius(value) {
        if (value <= 0) {
            throw new Error("Радиус должен быть положительным числом.");
        }
        this._radius = value;
    }

    get diameter() {
        return this._radius * 2;
    }

    area() {
        return Math.PI * Math.pow(this._radius, 2);
    }

    circumference() {
        return 2 * Math.PI * this._radius;
    }
}

const radius = prompt("введите радиус: ");
const circle = new Circle(radius)
console.log(`Диаметр: ${circle.diameter}`);
console.log(`Площадь: ${circle.area()}`);
console.log(`Длина окружности: ${circle.circumference()}`); 
