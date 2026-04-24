    document.addEventListener('DOMContentLoaded', function() {
        let x = prompt('введите число: ');

        if (x >= 0 && x <= 100) {
            alert(`${x} находится между 0 и 100`);
        } else if ( x> 100 && x < 200) {
            alert(`${x} находится между 100 и 200` );
        } else if (x > 200 && x < 300) {
            alert(`${x} находится мужду 200 и 300`);
        } else {
            alert(`${x} не попало ни в один диапозонов`)
        }
});