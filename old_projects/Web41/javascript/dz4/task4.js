const prompt = require('prompt-sync')();

function ploshad(len, shir){
    if (shir == undefined){
        return len * len;
    } else {
        return len * shir;
    }
}

let shir = parseInt(prompt('введите ширину числа(если квадрат нажмите enter): '));
let len = parseInt(prompt('введите длинну числа: '));
let s;
if (shir == ''){
    s = undefined;
}
const x = ploshad(len, s);
if (s == undefined){
    console.log(`площадь квадрата равна: ${x}`);
} else{
    console.log(`площадь прямоугольника равна:${x}`);
}