const prompt = require('prompt-sync')(); 

function f1(x) {
    return Math.pow(x, 4) + 2 * Math.pow(x, 3) - x - 1;
}

function f2(x) {
    return Math.pow(x, 3) - 0.2 * Math.pow(x, 2) - 0.2 * x - 1.2;
}

function bisectionMethod(func, a, b, epsilon = 0.001) {
    let mid;
    while ((b - a) / 2 > epsilon) {
        mid = (a + b) / 2;
        if (func(mid) === 0) {
            return mid;
        }
        if (func(a) * func(mid) < 0) {
            b = mid;
        } else {
            a = mid;
        }
    }
    return (a + b) / 2;
}

const root1 = bisectionMethod(f1, 0, 1);
console.log(`Приближенное значение корня для задачи а): ${root1}`);

const root2 = bisectionMethod(f2, 1, 1.5);
console.log(`Приближенное значение корня для задачи б): ${root2}`);