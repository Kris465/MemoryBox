const fourthSquare = document.getElementById('fourth');
const squares = document.querySelectorAll('.square:not(#fourth)');

squares.forEach(square => {
    square.addEventListener('mouseenter', () => {
        if (square.id === 'green') {
            fourthSquare.style.backgroundColor = 'green';
        } else if (square.id === 'yellow') {
            fourthSquare.style.backgroundColor = 'yellow';
        } else if (square.id === 'red') {
            fourthSquare.style.backgroundColor = 'red';
        }
    });

    square.addEventListener('mouseleave', () => {
        fourthSquare.style.backgroundColor = 'gray';
    });
});

document.body.addEventListener('mouseleave', () => {
    fourthSquare.style.backgroundColor = 'gray';
});
