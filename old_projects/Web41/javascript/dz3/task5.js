const prompt = require('prompt-sync')();

let nule = 0;
let plus = 0;
let minus = 0;
let chet = 0;
let nechet = 0;

for (let i = 1; i <= 10;i++){
    let x  = parseInt(prompt('Введите число : '));
    if (x > 0) plus++;
    else if (x < 0) minus++;
    else nule++ ;

    if (x % 2 == 0) chet++;
    else nechet++;  
}

console.log(`Нулей : ${nule}, Больше нуля : ${plus}, Меньше нуля : ${minus}, Четное : ${chet}, Нечетное : ${nechet}`);