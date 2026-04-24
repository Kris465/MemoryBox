function correctWord(word) {
    if (word === "глинянный") {
        return "глиняный";
    } else if (word === "граффика") {
        return "графика";
    } else {
        return word;
    }
}

let words = ["глинянный", "граффика"];
let correctedWords = words.map(correctWord);
console.log(correctedWords);