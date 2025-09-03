let timeoutId;

function submitForm() {
    document.querySelector('.message').innerText = 'Мы свяжемся с вами в ближайшее время.';
    document.querySelector('.message').style.display = 'block';
}

document.querySelector('.circle').addEventListener('mouseover', function() {
    clearTimeout(timeoutId); // Очищаем предыдущий таймаут, если он был запущен
    document.querySelector('.form-container').style.display = 'block';
});

document.querySelector('.circle').addEventListener('mouseleave', function() {
    timeoutId = setTimeout(function() {
        document.querySelector('.form-container').style.display = 'none';
    }, 2000); // Задержка в 2 секунды перед скрытием формы
});

document.querySelector('.form-container').addEventListener('mouseover', function() {
    clearTimeout(timeoutId); // Очищаем таймаут, если пользователь навел курсор на форму
});

document.querySelector('.form-container').addEventListener('mouseleave', function() {
    timeoutId = setTimeout(function() {
        document.querySelector('.form-container').style.display = 'none';
    }, 2000); // Задержка в 2 секунды перед скрытием формы
});
