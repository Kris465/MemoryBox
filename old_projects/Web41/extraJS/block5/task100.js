function swapLetters(word) {
    let letters = word.split('');

    if (letters.length >= 5) {
        let temp = letters[1];
        letters[1] = letters[4];
        letters[4] = temp;
    }

    return letters.join('');
}

let word = "пример";
let result = swapLetters(word);
console.log(result); 