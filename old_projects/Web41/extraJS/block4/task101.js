const prompt = require('prompt-sync')();

function findAverageOfMedians(triplet1, triplet2) {

    function findMedian(triplet) {

        triplet.sort((a, b) => a - b);

        return triplet[1];
    }

    const median1 = findMedian(triplet1);
    const median2 = findMedian(triplet2);


    const averageOfMedians = (median1 + median2) / 2;

    return averageOfMedians;
}

const triplet1 = [3.5, 1.2, 4.8];
const triplet2 = [7.0, 5.5, 6.3];

const result = findAverageOfMedians(triplet1, triplet2);
console.log("Среднее арифметическое средних чисел: ", result);