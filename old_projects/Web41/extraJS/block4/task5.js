
function function1(x) {
    return Math.sin(x);
}

function function2(x) {
    return x ** 2; 
}

function function3(x) {
    return 1 - 2 * Math.sin(x); 
}

function getY(x) {
    if (x < -1) {
        return function1(x); 
    } else if (x >= -1 && x < 1) {
        return function2(x); 
    } else {
        return function3(x); 
    }
}

const xValues = [-2, -0.5, 0, 1, 2]; 
xValues.forEach(x => {
    console.log(`x = ${x}, y = ${getY(x)}`);
});