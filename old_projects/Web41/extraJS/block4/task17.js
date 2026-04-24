const prompt = require('prompt-sync')();
function checkFit(circleArea, triangleArea) {

    const circleRadius = Math.sqrt(circleArea / Math.PI);


    const triangleSide = Math.sqrt((4 * triangleArea) / Math.sqrt(3));

    const inscribedCircleRadius = (triangleSide * Math.sqrt(3)) / 6;

    const circumscribedCircleRadius = triangleSide / Math.sqrt(3);

 
    const circleInTriangle = circleRadius <= inscribedCircleRadius;

    const triangleInCircle = circumscribedCircleRadius >= circleRadius;


    console.log(`Круг ${circleInTriangle ? "уместится" : "не уместится"} в равностороннем треугольнике.`);
    console.log(`Равносторонний треугольник ${triangleInCircle ? "уместится" : "не уместится"} в круге.`);
}


const circleArea = parseFloat(prompt("Введите площадь круга:"));
const triangleArea = parseFloat(prompt("Введите площадь равностороннего треугольника:"));

if (circleArea <= 0 || triangleArea <= 0) {
    console.log("Площади должны быть положительными числами.");
} else {

    checkFit(circleArea, triangleArea);
}