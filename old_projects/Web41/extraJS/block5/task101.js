function swapLetters(word) {
    let letters = word.split('');

    if (letters.length >= 3) {
        let temp = letters[2];
        letters[2] = letters[letters.length - 1];
        letters[letters.length - 1] = temp;
    }

    return letters.join('');
}


let word = "пример";
let result = swapLetters(word);
console.log(result);