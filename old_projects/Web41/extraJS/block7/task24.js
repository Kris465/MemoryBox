const prompt = require('prompt-sync')();


const childrenInClasses = [];


for (let i = 1; i <= 11; i++) {
    const input = prompt(`Введите число детей в ${i}-ом классе:`);
    const num = parseInt(input, 10);
    if (isNaN(num)) {
        alert("Пожалуйста, вводите числовое значение.");
        i--; 
    } else {
        childrenInClasses.push(num);
    }
}

let totalOddClassesChildren = 0;


for (let index = 0; index < childrenInClasses.length; index++) {
    
    if ((index + 1) % 2 !== 0) {
        totalOddClassesChildren += childrenInClasses[index];
    }
}

console.log("Общее число детей в первых, третьих, пятых и т. д. классах:", totalOddClassesChildren);