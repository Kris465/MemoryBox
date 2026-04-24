const prompt = require('prompt-sync')();

function calculateRectangles(a, b, c, d) {

    if (a <= b || c <= d) {
        console.log("Пожалуйста, убедитесь, что a > b и c > d.");
        return;
    }


    const count1 = Math.floor(a / c) * Math.floor(b / d);

    const count2 = Math.floor(a / d) * Math.floor(b / c);

    console.log(`Количество прямоугольников при размещении вдоль длинной стороны стола: ${count1}`);
    console.log(`Количество прямоугольников при размещении вдоль короткой стороны стола: ${count2}`);


    if (count1 > count2) {
        console.log("Большее количество прямоугольников можно разместить вдоль длинной стороны стола.");
    } else if (count2 > count1) {
        console.log("Большее количество прямоугольников можно разместить вдоль короткой стороны стола.");
    } else {
        console.log("Количество прямоугольников одинаково в обеих ориентациях.");
    }
}


let a = parseInt(prompt("Введите длину стола (a):"));
let b = parseInt(prompt("Введите ширину стола (b):"));
let c = parseInt(prompt("Введите длину прямоугольника (c):"));
let d = parseInt(prompt("Введите ширину прямоугольника (d):"));

if (!isNaN(a) && !isNaN(b) && !isNaN(c) && !isNaN(d)) {
    calculateRectangles(a, b, c, d);
} else {
    console.log("Пожалуйста, введите корректные целые числа.");
}