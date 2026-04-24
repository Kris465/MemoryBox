const prompt = require('prompt-sync')();

let dlina = prompt('введите длинну');
let shirina = prompt('введите ширину')

let P = (dlina * 2 + shirina * 2 );
let D = Math.sqrt(dlina * dlina + shirina * shirina );
console.log(`периметр равен: ${P}, гипотенуза равна: ${D}`);