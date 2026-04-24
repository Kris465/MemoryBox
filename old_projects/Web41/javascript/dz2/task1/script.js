document.getElementById('ageButton').addEventListener('click', function() {
    const age = Number(document.getElementById('ageInput').value);
    const ageResult = document.getElementById('ageResult');

    if (age >= 0 && age < 12) {
        ageResult.textContent = 'Вы ребенок';
    } else if (age >= 12 && age <= 18) {
        ageResult.textContent = 'Вы подросток';
    } else if (age > 18 && age < 60) {
        ageResult.textContent = 'Вы взрослый';
    } else if (age >= 60 && age < 120) {
        ageResult.textContent = 'Вы пенсионер';
    } else {
        ageResult.textContent = 'Некорректный возраст';
    }
});