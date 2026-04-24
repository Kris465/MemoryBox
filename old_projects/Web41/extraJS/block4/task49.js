const prompt = require('prompt-sync')();

function solveQuadraticEquation(a, b, c) {
    if (a === 0) {
        throw new Error("Коэффициент a не должен быть равен 0.");
    }

    const D = b * b - 4 * a * c;

    if (D > 0) {
        const x1 = (-b + Math.sqrt(D)) / (2 * a);
        const x2 = (-b - Math.sqrt(D)) / (2 * a);
        return { roots: [x1, x2], count: 2 };
    } else if (D === 0) {
        const x = -b / (2 * a);
        return { roots: [x], count: 1 };
    } else {
        return { roots: [], count: 0 };
    }
}

const a = 1;
const b = -3; 
const c = 2; 
const result = solveQuadraticEquation(a, b, c);
console.log(`Количество корней: ${result.count}`);
if (result.count > 0) {
    console.log(`Корни: ${result.roots}`);
} else {
    console.log("Нет действительных корней.");
}