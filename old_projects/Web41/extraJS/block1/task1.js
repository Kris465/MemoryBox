let pi = Math.PI
function roundTo(num, places) {
    const factor = Math.pow(10, places);
    return Math.round(num * factor) / factor;
}

let roundedToTwoDecimals = roundTo(pi, 2);
console.log(`${roundedToTwoDecimals}`);