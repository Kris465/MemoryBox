let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.carousel-images img');
    if (index >= slides.length) {
        currentSlide = 0;
    } else if (index < 0) {
        currentSlide = slides.length - 1;
    } else {
        currentSlide = index;
    }
    
    const offset = -currentSlide * 100; // Сдвиг в процентах
    document.querySelector('.carousel-images').style.transform = translateX(`${offset}%`);
}

function moveSlide(direction) {
    showSlide(currentSlide + direction);
}

// Инициализация первой слайд
showSlide(currentSlide);
