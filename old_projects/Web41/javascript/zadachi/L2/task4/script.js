document.addEventListener('DOMContentLoaded', function() {
    let chislo1 = prompt('введите число: ');
    let chislo2 = prompt('введите число: ');

    if (chislo1 > chislo2){
        alert(`${chislo1} > ${chislo2} `);
    } else if (chislo1 < chislo2){
        alert(`${chislo1} < ${chislo2} `);
    } else {
        alert(`${chislo1} = ${chislo2} `);
    }
});