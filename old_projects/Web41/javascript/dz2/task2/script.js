document.getElementById('symvolButton').addEventListener('click', function() {
    const symvol = Number(document.getElementById('symvolInput').value);
    const symvolResult = document.getElementById('symvolResult');

    if (symvol == 0){
        symvolResult.textContent = ')';
    } else if (symvol == 1){
        symvolResult.textContent = '!';
    } else if (symvol == 2){
        symvolResult.textContent = '@';
    } else if (symvol == 3){
        symvolResult.textContent = '#';
    } else if (symvol == 4){
        symvolResult.textContent = '$';
    } else if (symvol == 5){
        symvolResult.textContent = '%';
    } else if (symvol == 6){
        symvolResult.textContent = '^';
    } else if (symvol == 7){
        symvolResult.textContent = '&';
    } else if (symvol == 8){
        symvolResult.textContent = '*';
    } else if (symvol == 9){
        symvolResult.textContent = '(';
    }
});