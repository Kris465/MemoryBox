for (let x = 4; x <= 6; x++) {
    let yStart = 4;
    let yEnd = (x === 6) ? 4 : 8; 
    for (let y = yStart; y <= yEnd; y += 2) {
        console.log(`${x},${y}`);
    }
}