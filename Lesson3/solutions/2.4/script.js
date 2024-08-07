function validateYear() {
    const yearInput = document.getElementById('year');
    const year = parseInt(yearInput.value);

    if (year < 0) {
        alert("Пожалуйста, введите положительный год.");
        return false;
    }
    
    return true;
}
