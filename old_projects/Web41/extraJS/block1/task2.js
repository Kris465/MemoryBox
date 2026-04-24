const e = Math.E
console.log(e)
function roundTo(num, places) {
    const factor = Math.pow(10, places);
    return Math.round(num * factor) / factor;
}

let roundedToTwoDecimals = roundTo(e, 2);
console.log(`${roundedToTwoDecimals}`);