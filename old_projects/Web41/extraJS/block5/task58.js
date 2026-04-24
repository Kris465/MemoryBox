
let athlete1Scores = [85, 90, 78, 92, 88]; 
let athlete2Scores = [80, 85, 90, 95, 87];


function calculateTotalScore(scores) {
    let total = 0;
    for (let i = 0; i < scores.length; i++) {
        total += scores[i];
    }
    return total;
}


let athlete1Total = calculateTotalScore(athlete1Scores);
let athlete2Total = calculateTotalScore(athlete2Scores);

console.log("Сумма баллов первого спортсмена:", athlete1Total);
console.log("Сумма баллов второго спортсмена:", athlete2Total);
