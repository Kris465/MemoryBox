document.querySelectorAll('.gallery-item').forEach(item => {
    item.addEventListener('click', event => {
        const lightbox = document.getElementById('lightbox');
        const lightboxImg = document.getElementById('lightbox-img');
        
        lightbox.style.display = 'flex';
        lightboxImg.src = item.src;
    });
});

document.querySelector('.close').addEventListener('click', () => {
    const lightbox = document.getElementById('lightbox');
    lightbox.style.display = 'none';
});

document.getElementById('lightbox').addEventListener('click', (event) => {
    if (event.target === event.currentTarget) {
        event.currentTarget.style.display = 'none';
    }
});
