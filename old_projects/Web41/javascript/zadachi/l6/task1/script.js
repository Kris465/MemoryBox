const text = "To be, or not to be, that is the question...";
const author = 'William Shakespeare, from "Hamlet"';

let index = 0;

function writeText() {
    const container = document.getElementById('text-container');

    if (index < text.length) {
        container.innerHTML += text[index];
        index++;
        setTimeout(writeText, 200);
    } else {
        container.innerHTML += "<br><span class='author'>";
        writeAuthor();
    }
}

function writeAuthor() {
    const container = document.getElementById('text-container');
    let authorIndex = 0;

    function writeNextLetter() {
        if (authorIndex < author.length) {
            container.innerHTML += author[authorIndex];
            authorIndex++;
            setTimeout(writeNextLetter, 200);
        }
    }

    writeNextLetter();
}

writeText();