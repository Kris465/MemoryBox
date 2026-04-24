function divideIntegers(m, n) {
    if (n === 0) {
        console.log("Деление на ноль невозможно.");
        return;
    }

    if (m % n === 0) {
        console.log(m / n);
    } else {
        console.log("m на n нацело не делится");
    }
}


let m = 10; 
let n = 2;  
divideIntegers(m, n);