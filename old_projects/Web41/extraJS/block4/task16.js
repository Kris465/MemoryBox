const prompt = require('prompt-sync')();

function checkFit(circleArea, squareArea) {

    const circleRadius = Math.sqrt(circleArea / Math.PI);
    const circleDiameter = 2 * circleRadius;

    const squareSide = Math.sqrt(squareArea);
    const squareDiagonal = squareSide * Math.sqrt(2);

    const circleInSquare = circleDiameter <= squareSide;
    const squareInCircle = squareDiagonal <= circleDiameter;

    console.log(`Круг ${circleInSquare ? "уместится" : "не уместится"} в квадрате.`);
    console.log(`Квадрат ${squareInCircle ? "уместится" : "не уместится"} в круге.`);
}

const circleArea = parseFloat(prompt("Введите площадь круга:"));
const squareArea = parseFloat(prompt("Введите площадь квадрата:"));

if (circleArea <= 0 || squareArea <= 0) {
    console.log("Площади должны быть положительными числами.");
} else {
    checkFit(circleArea, squareArea);
}