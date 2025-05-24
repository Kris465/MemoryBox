var swiper = new Swiper('.swiper-container', {
    loop: true, // Зацикливаем слайды
    slidesPerView: 1, // Сколько слайдов будет показываться одновременно
    spaceBetween: 10, // Расстояние между слайдами
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
    pagination: {
      el: '.swiper-pagination',
      clickable: true, // Сделать индикаторы кликабельными
    },
    autoplay: {
      delay: 3000, // Автоматическая прокрутка с интервалом 3 секунды
    },
  });
  