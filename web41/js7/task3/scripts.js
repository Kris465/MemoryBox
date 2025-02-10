const block1 = document.getElementById('block1');
const block2 = document.getElementById('block2');
const block3 = document.getElementById('block3');

function moveBlock(block, event) {
    const x = event.clientX;
    const y = event.clientY;

    block.style.left = `${x - block.offsetWidth / 2}px`;
    block.style.top = `${y - block.offsetHeight / 2}px`;
}
document.addEventListener('mousedown', (event) => {
    switch (event.button) {
        case 0:
            moveBlock(block1, event);
            break;
        case 1:
            moveBlock(block2, event);
            break;
        case 2:
            moveBlock(block3, event);
            break;
    }
});

document.addEventListener('contextmenu', (event) => {
    event.preventDefault();
});
