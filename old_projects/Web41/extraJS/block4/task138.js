function getDigitInSequence(n) {
    if (n < 1 || n > 32) return -1; 

    let countDigits = 0;

    for (let num = 0; num <= 20; num++) {
        let digitsInNum = (num < 10) ? 1 : 2;

        if (countDigits + digitsInNum >= n) {
            let posInNum = n - countDigits; 

            if (digitsInNum === 1) {
                return num; 
            } else {
                if (posInNum === 1) {
                    return Math.floor(num /10); 
                } else {
                    return num %10; 
                }
            }
        }
        countDigits += digitsInNum;
    }

    return -1; 
}


let n = parseInt(prompt("Введите номер цифры n (1..32):"),10);
let digit = getDigitInSequence(n);
if(digit === -1){
    console.log("Ошибка: n вне диапазона");
} else {
    console.log(`Цифра под номером ${n} равна ${digit}`);
}