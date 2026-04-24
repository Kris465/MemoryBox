const prompt = require('prompt-sync')();

function canFitRectangle(a, b, c, d) {
 
    return (a <= c && b <= d) || (a <= d && b <= c);
}


function getInput() {
    const a = parseFloat(prompt("Введите длину первой стороны прямоугольника (a):"));
    const b = parseFloat(prompt("Введите длину второй стороны прямоугольника (b):"));
    const c = parseFloat(prompt("Введите длину первой стороны внешнего прямоугольника (c):"));
    const d = parseFloat(prompt("Введите длину второй стороны внешнего прямоугольника (d):"));

   
    if (a <= 0 || b <= 0 || c <= 0 || d <= 0) {
        console.log("Все числа должны быть положительными.");
        return;
    }

   
    const result = canFitRectangle(a, b, c, d);
    if (result) {
        console.log(`Прямоугольник со сторонами ${a} и ${b} можно уместить внутри прямоугольника со сторонами ${c} и ${d}.`);
    } else {
        console.log(`Прямоугольник со сторонами ${a} и ${b} нельзя уместить внутри прямоугольника со сторонами ${c} и ${d}.`);
    }
}


getInput();