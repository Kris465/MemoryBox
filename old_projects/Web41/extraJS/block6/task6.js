
const sequence = [];
const n = ];

const sequence = [1.2, 3.4, 5.6, 7.8, 9.0, 10.2, 12.4, 14.6, 16.8, 18.0, 20.2, 22.4, 24.6, 26.8, 28.0];
const n = 15;

let sumLessThanN = 0;
for (let i = 0; i < sequence.length; i++) {
    if (sequence[i] < n) {
        sumLessThanN += sequence[i];
    } else {
        break; 
    }
}
console.log("Сумма элементов меньше n:", sumLessThanN);
function binarySearch(arr, target) {
    let left = 0;
    let right = arr.length -1;
    while (left <= right) {
        const mid = Math.floor((left + right) /2);
        if (arr[mid] === target) {
            return mid; 
        } else if (arr[mid] < target) {
            left = mid +1;
        } else {
            right = mid -1;
        }
    }
    return left;
}

const position = binarySearch(sequence, n);
if (position > 0 && position < sequence.length) {
    const lowerIndex = position -1;
    const upperIndex = position;
    console.log(`n находится между элементами с индексами ${lowerIndex} и ${upperIndex}:`);
    console.log(`a${lowerIndex +1} = ${sequence[lowerIndex]}, a${upperIndex +1} = ${sequence[upperIndex]}`);
} else {
    console.log("Не удалось определить интервал для n");
}