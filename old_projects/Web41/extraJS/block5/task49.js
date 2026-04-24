function sumOfSquares(numbers) {

    const sum = numbers.reduce((accumulator, current) => accumulator + (current ** 2), 0);
    return sum;
}

const n = 3; 
const numbers = [1.5, 2.3, 3.7]; 

if (numbers.length !== n) {
    console.error(`Количество введенных чисел (${numbers.length}) не соответствует n (${n}).`);
} else {
    const result = sumOfSquares(numbers);
    console.log(`Сумма квадратов вещественных чисел: ${result}`); 
}