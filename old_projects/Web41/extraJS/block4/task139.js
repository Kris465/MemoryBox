const prompt = require('prompt-sync')();

function getDigit(k) {
    if (k <1 || k >252) return -1; 

    if (k <=100) {

        let numIndex = Math.ceil(k /2); 
        let num = 50 + numIndex -1;

        if (k %2 ===1) {
    
            return Math.floor(num /10);
        } else {

            return num %10;
        }
    } else {

        let k2 = k -100;
        let numIndex = Math.ceil(k2 /3); 
        let num = 100 + numIndex -1;

        let posInNum = k2 %3;
        if (posInNum ===0) posInNum =3;

        if (posInNum ===1) {
            return Math.floor(num /100);
        } else if (posInNum ===2) {
            return Math.floor((num %100)/10);
        } else { 
            return num %10;
        }
    }
}

let k = parseInt(prompt("Введите номер цифры k (1..252):"),10);
let digit = getDigit(k);
if(digit === -1){
    console.log("Ошибка: k вне диапазона");
} else {
    console.log(`Цифра под номером ${k} равна ${digit}`);
}