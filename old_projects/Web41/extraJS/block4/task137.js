function getDigit(k) {
    if (k < 1 || k > 180) {
        return -1; 
    }
    let numIndex = Math.ceil(k / 2); 
    let number = numIndex + 9;

    if (k % 2 === 1) {
        
        return Math.floor(number / 10);
    } else {
        
        return number % 10;
    }
}


let k = parseInt(prompt("Введите k (1..180):"),10);
let digit = getDigit(k);
if(digit === -1) {
    console.log("Ошибка: k вне диапазона");
} else {
    console.log(`Цифра под номером ${k} равна ${digit}`);
}