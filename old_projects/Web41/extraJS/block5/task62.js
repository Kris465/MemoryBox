const prompt = require('prompt-sync')();

function calculateAverageGrade(grades) {
    const totalGrades = grades.reduce((sum, grade) => sum + grade, 0);
    return totalGrades / grades.length;
}

const classAGrades = [4, 5, 3, 4, 5];
const classBGrades = [3, 4, 4, 5, 3];

const averageGradeClassA = calculateAverageGrade(classAGrades);
const averageGradeClassB = calculateAverageGrade(classBGrades);

console.log(`Средняя оценка учеников класса A: ${averageGradeClassA.toFixed(2)}`);
console.log(`Средняя оценка учеников класса B: ${averageGradeClassB.toFixed(2)}`);