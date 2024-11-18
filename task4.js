// const prompt = require('prompt-sync')();

// function uniqueElements(arr1, arr2) {
//     const uniqueArray = [];

//     for (let i = 0; i < arr1.length; i++) {
//         let isUnique = true;
//         for (let j = 0; j < arr2.length; j++) {
//             if (arr1[i] === arr2[j]) {
//                 isUnique = false;
//                 break;
//             }
//         }
//         if (isUnique) {
//             uniqueArray.push(arr1[i]);
//         }
//     }

//     for (let i = 0; i < arr2.length; i++) {
//         let isUnique = true;
//         for (let j = 0; j < arr1.length; j++) {
//             if (arr2[i] === arr1[j]) {
//                 isUnique = false;
//                 break;
//             }
//         }
//         if (isUnique) {
//             uniqueArray.push(arr2[i]);
//         }
//     }
//     return uniqueArray;
// }

// const input1 = prompt("Введите первый массив через запятую: ");
// const input2 = prompt("Введите второй массив через запятую: ");

// const array1 = input1.split(',').map(Number);
// const array2 = input2.split(',').map(Number);

// const result = uniqueElements(array1, array2);

// console.log("Результат: ", result);

const prompt = require('prompt-sync')();

function uniqueElements(arr1, arr2) {
    const set1 = new Set(arr1);
    const set2 = new Set(arr2);

    const uniqueInFirst = [...set1].filter(x => !set2.has(x));
    const uniqueInSecond = [...set2].filter(x => !set1.has(x));

    return [...uniqueInFirst, ...uniqueInSecond];
}

const input1 = prompt("Введите первый массив: ");
const input2 = prompt("Введите второй массив: ");

const array1 = input1.split(',').map(Number);
const array2 = input2.split(',').map(Number);

const result = uniqueElements(array1, array2);

console.log("Результат: ", result);
