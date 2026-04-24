function swapLetters(word, m, n) {
    let letters = word.split('');

    if (m >= 1 && n >= 1 && m <= letters.length && n <= letters.length) {
        let temp = letters[m - 1];
        letters[m - 1] = letters[n - 1];
        letters[n - 1] = temp;
    } else {
        console.log("Индексы выходят за пределы длины слова.");
    }

    return letters.join('');
}

let word = "пример";
let m = 3;
let n = 6;
let result = swapLetters(word, m, n);
console.log(result);