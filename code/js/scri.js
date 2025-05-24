document.addEventListener('DOMContentLoaded', function() {
    const slider = document.querySelector('.slider-container');
    const slides = document.querySelectorAll('.slide');
    const prevBtn = document.querySelector('.slider-prev');
    const nextBtn = document.querySelector('.slider-next');
    
    let currentSlide = 0;
    const slideCount = slides.length;
    let isAnimating = false;
    let autoSlideDirection = 1; // 1 - вперед, -1 - назад
    const animationDuration = 500; // Длительность анимации в ms
    const slideInterval = 2780; // Интервал между слайдами
    
    // Инициализация слайдера
    function initSlider() {
      // Клонируем первый и последний слайды для бесконечного эффекта
      const firstClone = slides[0].cloneNode(true);
      const lastClone = slides[slideCount-1].cloneNode(true);
      
      slider.appendChild(firstClone);
      slider.insertBefore(lastClone, slides[0]);
      
      // Обновляем список слайдов
      const updatedSlides = document.querySelectorAll('.slide');
      
      // Устанавливаем начальную позицию
      currentSlide = 1;
      slider.style.transform = `translateX(-${currentSlide * slides[0].clientWidth}px)`;
      slider.style.transition = `transform ${animationDuration}ms ease`;
      
      updateButtons();
    }
    
    // Обновление позиции слайдера
    function updateSlider(direction, callback) {
      if (isAnimating) return;
      isAnimating = true;
      
      const slideWidth = slides[0].clientWidth;
      currentSlide += direction;
      
      slider.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
      
      // Проверка на границы для бесконечного эффекта
      setTimeout(() => {
        if (currentSlide === 0) {
          // Переход к "фейковому" последнему слайду
          slider.style.transition = 'none';
          currentSlide = slideCount;
          slider.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
          setTimeout(() => {
            slider.style.transition = `transform ${animationDuration}ms ease`;
          }, 50);
        } else if (currentSlide === slideCount + 1) {
          // Переход к "фейковому" первому слайду
          slider.style.transition = 'none';
          currentSlide = 1;
          slider.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
          setTimeout(() => {
            slider.style.transition = `transform ${animationDuration}ms ease`;
          }, 50);
        }
        
        isAnimating = false;
        if (callback) callback();
      }, animationDuration);
    }
    
    // Обновление состояния кнопок
    function updateButtons() {
      // Для бесконечного слайдера кнопки всегда активны
      prevBtn.disabled = false;
      nextBtn.disabled = false;
    }
    
    // Переход к следующему слайду
    function nextSlide() {
      updateSlider(1, () => {
        autoSlideDirection = 1; // Продолжаем движение вперед
      });
    }
    
    // Переход к предыдущему слайду
    function prevSlide() {
      updateSlider(-1, () => {
        autoSlideDirection = -1; // Продолжаем движение назад
      });
    }
    
    // Автопрокрутка с изменением направления
    function autoSlide() {
      if (autoSlideDirection === 1) {
        nextSlide();
      } else {
        prevSlide();
      }
    }
    
    // Обработчики событий
    nextBtn.addEventListener('click', nextSlide);
    prevBtn.addEventListener('click', prevSlide);
    
    // Автопрокрутка
    let autoSlideTimer = setInterval(autoSlide, slideInterval);
    
    // Пауза при наведении
    slider.parentElement.addEventListener('mouseenter', () => {
      clearInterval(autoSlideTimer);
    });
    
    slider.parentElement.addEventListener('mouseleave', () => {
      autoSlideTimer = setInterval(autoSlide, slideInterval);
    });
    
    // Инициализация
    initSlider();
    
    // Ресайз окна
    window.addEventListener('resize', () => {
      const slideWidth = slides[0].clientWidth;
      slider.style.transform = `translateX(-${currentSlide * slideWidth}px)`;
    });
  });