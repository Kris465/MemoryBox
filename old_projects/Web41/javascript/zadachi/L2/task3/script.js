document.addEventListener('DOMContentLoaded', function() {
    let chislo = prompt('введите число: ');

    if (chislo >= 0 && chislo <= 100) {
        alert(`${chislo} принадлежит диапозону от 0 до 100`);
    } else {
        alert(`${chislo} не принадлежит диапозону от 0 до 100`);
    }
});