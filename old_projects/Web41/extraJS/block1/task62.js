const prompt = require('prompt-sync')();



function calculat (a) {
    let a3 = a * a * a;
    let a10 = a3 * a3 * a3 * a;

    console.log(`a) a^3 = ${a3}, a^10 = ${a10}`);

    let b2 = a * a;
    let b4 = b2 * b2;
    let b10 = b4 * b4 *b2;
    let b20 = b10 * b10;
    console.log(`b) a^4 = ${b4}, a^20 = ${b20}`);

    let c2 = a * a;
    let c5 = c2 * c2 * a;
    let c13 = c5 * c5 * c2 * a;

    console.log(`c) a^5 = ${c5}, a^13 = ${c13}`);

    let d2 = a * a;
    let d5 = d2 * d2 * a;
    let d19 = d5 * d5 * d5 * d2 * d2;

    console.log(`d) a^5 = ${d5}, a^19 = ${d19}`);

    let e2 = a * a;
    let e5 = e2 * e2 * a;
    let e17 = d5 * d5 * d5 * d2;

    console.log(`e) a^2 = ${e2} a^5 = ${e5}, a^17 = ${e17}`);

    let f2 = a * a;
    let f4 = f2 * f2;
    let f12 = f4 * f4 * f4;
    let f28 = f12* f12 * f4;

    console.log(`f) a^4 = ${f4} a^12 = ${f12}, a^28 = ${f28}`);

}

const a = prompt('Введите число: ');
calculat(a);