function calculateY(x) {
    if (x > 0) {
        return Math.sin(x) ** 2; 
    } else {
        return 1 - 2 * (Math.sin(x) ** 2); 
    }
}

console.log(calculateY(1));  
console.log(calculateY(0));  
console.log(calculateY(-1)); 