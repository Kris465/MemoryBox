document.getElementById('yearButton').addEventListener('click', function() {
    const year = document.getElementById('yearInput').value;
    const yearResult = document.getElementById('yearResult');

    if ((year % 400 == 0) ||(year % 4 == 0 && year % 100 != 0)) {
        yearResult.textContent = 'високосный';
    } else {
        yearResult.textContent = 'обычный';
    }

});