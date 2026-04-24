const points = [3, 0, 1, 3, 1, 0, 3, 1]; 

let wins = 0;
let losses = 0;
let draws = 0;

for (let point of points) {
    if (point === 3) {
        wins++;
    } else if (point === 0) {
        losses++;
    } else if (point === 1) {
        draws++;
    }
}

console.log(`Побед: ${wins}`);
console.log(`Поражений: ${losses}`);
console.log(`Ничьих: ${draws}`);