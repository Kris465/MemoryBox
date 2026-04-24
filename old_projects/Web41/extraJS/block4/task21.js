function isDivisor(a, b) {
    if (a === 0) {
        console.log("Деление на ноль невозможно.");
        return;
    }

    if (b % a === 0) {
        console.log(`${a} является делителем ${b}`);
    } else {
        console.log(`${a} не является делителем ${b}`);
    }
}

let a = 3; 
let b = 9; 
isDivisor(a, b);