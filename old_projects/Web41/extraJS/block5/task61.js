const prompt = require('prompt-sync')();

function calculateAverageHeight(heights) {
    const totalHeight = heights.reduce((sum, height) => sum + height, 0);
    return totalHeight / heights.length;
}

const classAHeights = [160, 165, 170, 175, 180];
const classBHeights = [155, 162, 168, 172, 178];

const averageHeightClassA = calculateAverageHeight(classAHeights);
const averageHeightClassB = calculateAverageHeight(classBHeights);

console.log(`Средний рост учеников класса A: ${averageHeightClassA.toFixed(2)} см`);
console.log(`Средний рост учеников класса B: ${averageHeightClassB.toFixed(2)} см`);