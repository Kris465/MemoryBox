const prompt = require('prompt-sync')();  

const grades = [3, 4, 2, 5, 3, 4, 2, 5, 4, 3, 2, 4, 5, 3, 4, 2, 5, 3, 4, 2, 5, 4, 3, 2, 4, 5, 3, 4];

let hasTwo = false;
for (let i = 0; i < grades.length; i++) {
    if (grades[i] === 2) {
        hasTwo = true;
        break;
    }
}

if (hasTwo) {
    console.log("В списке есть оценки двойки.");
} else {
    console.log("В списке нет оценок двойки.");
}