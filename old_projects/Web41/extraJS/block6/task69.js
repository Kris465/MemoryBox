const prompt = require('prompt-sync')(); 

const sequence = [ 1.2, 3.4, 3.4, 5.6, 7.8, 9.0, 10.1, 12.3, 14.5, 16.7, 18.9, 20.0, 22.2, 24.4, 26.6];

function checkAscendingOrder(arr) {
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] > arr[i + 1]) {
            return i + 1; 
        }
    }
    return -1;
}

const violationIndex = checkAscendingOrder(sequence);

if (violationIndex === -1) {
    console.log("Последовательность упорядочена по возрастанию.");
} else {
    console.log(`Последовательность не упорядочена по возрастанию. Нарушение в позиции ${violationIndex}.`);
}