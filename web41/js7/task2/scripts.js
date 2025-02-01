const movableBlock = document.getElementById('movableBlock');

function moveBlock(event) {
    const x = event.clientX;
    const y = event.clientY;
    movableBlock.style.left = `${x - movableBlock.offsetWidth / 2}px`;
    movableBlock.style.top = `${y - movableBlock.offsetHeight / 2}px`;
}

document.addEventListener('click', moveBlock);
