
let student1Grades = [4, 5, 3, 4]; 
let student2Grades = [5, 4, 4, 3]; 

function calculateSum(grades) {
    let sum = 0;
    for (let i = 0; i < grades.length; i++) {
        sum += grades[i];
    }
    return sum;
}

let student1Sum = calculateSum(student1Grades);
let student2Sum = calculateSum(student2Grades);

console.log("Сумма оценок первого ученика:", student1Sum);
console.log("Сумма оценок второго ученика:", student2Sum);