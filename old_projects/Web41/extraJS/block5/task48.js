function sumOfSquares(numbers) {

    const sum = numbers.reduce((accumulator, current) => accumulator + (current ** 2), 0);
    return sum;
}

const numbers = [1, 2, 10]; 

const result = sumOfSquares(numbers);
console.log(`Сумма квадратов чисел: ${result}`); 