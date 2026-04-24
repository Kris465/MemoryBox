document.addEventListener('DOMContentLoaded', function() {
    let chislo = prompt('введите число: ');

    if (chislo == 0){
        alert(`${chislo} будет ноль`)
    } else if (chislo == 1){
        alert(`${chislo} будет один`)
    } else if (chislo == 2){
        alert(`${chislo} будет два`)
    } else if (chislo == 3){
        alert(`${chislo} будет три`)
    } else if (chislo == 4){
        alert(`${chislo} будет четыре`)
    } else if (chislo == 5){
        alert(`${chislo} будет пять`)
    } else if (chislo == 6){
        alert(`${chislo} будет шесть`)
    } else if (chislo == 7){
        alert(`${chislo} будет семь`)
    } else if (chislo == 8){
        alert(`${chislo} будет восемь`)
    } else if (chislo == 9){
        alert(`${chislo} будет девять`)
    } else {
        alert(`не цифра`);
    }
});