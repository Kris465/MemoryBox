function calculateY(x) {
    if (x > 0) {
        return Math.sin(x) ** 2;
    } else {
        return 1 - 2 * (Math.sin(x) ** 2); 
    }
}

const xValues = [1, 0, -1, -Math.PI / 2, Math.PI / 2]; 
xValues.forEach(x => {
    console.log(`x = ${x}, y = ${calculateY(x)}`);
});