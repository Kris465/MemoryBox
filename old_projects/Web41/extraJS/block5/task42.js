function totalScore(scores) {

    if (scores.length !== 4) {
        console.error("Количество оценок должно быть равно 4.");
        return null;
    }

    const total = scores.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    return total;
}

const scores = [85, 90, 78, 92]; 

const result = totalScore(scores);
if (result !== null) {
    console.log("Сумма набранных баллов:", result);
}