const prompt = require('prompt-sync')();

let radius = prompt("введите радиус круга: ");

let dlina = (2 * radius * Math.PI);
let S = (Math.PI * Math.sqrt(radius))

console.log(`длина круга равна: ${dlina}, а площадь круга равна: ${S}`);