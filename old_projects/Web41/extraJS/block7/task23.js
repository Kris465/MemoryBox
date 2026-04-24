const prompt = require('prompt-sync')();

const rainfall = [/* вставьте сюда данные, например: */ 5, 10, 0, 3, 8, 2, 4, 7, 1, 6]; 

let totalPrecipitation = 0;

for (let day = 0; day < rainfall.length; day++) {

    if ((day + 1) % 2 === 0) {
        totalPrecipitation += rainfall[day];
    }
}

console.log("Общее количество осадков за второе, четвёртое и т.д. число месяца:", totalPrecipitation);