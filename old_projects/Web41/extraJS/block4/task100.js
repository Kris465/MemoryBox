//artemka malenkaya popka
function productOfTwoSmallest(a, b, c) {
    let smallest, secondSmallest;


    if (a < b && a < c) {
        smallest = a;
        secondSmallest = Math.min(b, c);
    } else if (b < a && b < c) {
        smallest = b;
        secondSmallest = Math.min(a, c);
    } else {
        smallest = c;
        secondSmallest = Math.min(a, b);
    }

 
    return smallest * secondSmallest;
}


const num1 = parseFloat(prompt("Введите первое число:"));
const num2 = parseFloat(prompt("Введите второе число:"));
const num3 = parseFloat(prompt("Введите третье число:"));


if (num1 === num2 || num1 === num3 || num2 === num3) {
    console.log("Числа должны быть различными.");
} else {
    const product = productOfTwoSmallest(num1, num2, num3);
    
    console.log(`Произведение двух наименьших чисел: ${product}`);
}