document.getElementById('numButton').addEventListener('click', function() {
    const num = document.getElementById('numInput').value;
    const numResult = document.getElementById('numResult');

    if (num.length === 3) {
        const digits = num.split(''); 
        const dublicates = new Set(digits).size !== digits.length;
        if (dublicates) {
            numResult.textContent = 'в числе есть одинаковые цифры';
        } else {
            numResult.textContent = 'в числе нет одинаковых цифр';
        }
    } else {
        numResult.textContent = 'число не трёхзначное';
    }

});
