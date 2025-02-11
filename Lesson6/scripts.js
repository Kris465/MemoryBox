function caesarCipher(text, shift) {
    const result = [];
    
    for (let char of text) {
        let code = char.charCodeAt(0);
        
        if (code >= 65 && code <= 90) {
            result.push(String.fromCharCode(((code - 65 + shift) % 26) + 65));
        } else if (code >= 97 && code <= 122) {
            result.push(String.fromCharCode(((code - 97 + shift) % 26) + 97));
        } 
        else if (code >= 1040 && code <= 1071) {
            result.push(String.fromCharCode(((code - 1040 + shift) % 32) + 1040));
        } else if (code >= 1072 && code <= 1103) {
            result.push(String.fromCharCode(((code - 1072 + shift) % 32) + 1072));
        } else {
            result.push(char);
        }
    }
    
    return result.join('');
}

document.getElementById('encryptBtn').addEventListener('click', function() {
    const inputText = document.getElementById('inputText').value;
    const shift = parseInt(document.getElementById('shift').value);
    const result = caesarCipher(inputText, shift);
    
    document.getElementById('result').textContent = result;
});

document.getElementById('decryptBtn').addEventListener('click', function() {
    const inputText = document.getElementById('inputText').value;
    const shift = parseInt(document.getElementById('shift').value);
    const result = caesarCipher(inputText, -shift);
    
    document.getElementById('result').textContent = result;
});
