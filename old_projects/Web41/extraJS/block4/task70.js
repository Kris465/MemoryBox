function maxOfTwo(a, b) {
    const isAGreater = a > b ? true : false;
    const max = isAGreater ? a : b; 

    return max;
}

const num1 = 5.5;
const num2 = 3.2;
console.log(maxOfTwo(num1, num2)); 