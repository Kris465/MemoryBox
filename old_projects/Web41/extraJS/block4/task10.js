const prompt = require('prompt-sync')();

function circleArea(radius) {
    return Math.PI * Math.pow(radius, 2); 
}

function squareArea(side) {
    return Math.pow(side, 2);
}

function compareAreas(radius, side) {
    const areaCircle = circleArea(radius); 
    const areaSquare = squareArea(side);

    console.log(`Площадь круга: ${areaCircle.toFixed(4)}`);
    console.log(`Площадь квадрата: ${areaSquare.toFixed(4)}`);

    if (areaCircle > areaSquare) {
        console.log("Площадь круга больше площади квадрата.");
    } else if (areaCircle < areaSquare) {
        console.log("Площадь квадрата больше площади круга.");
    } else {
        console.log("Площади круга и квадрата равны.");
    }
}

const radius = parseFloat(prompt("Введите радиус круга:"));
const side = parseFloat(prompt("Введите сторону квадрата:"));

compareAreas(radius, side);