document.getElementById('submitReview').addEventListener('click', function() {
    var reviewInput = document.getElementById('reviewInput').value;
    var reviewMessage = document.getElementById('message');
    
    if (!reviewInput.trim()) {
        Document.getElementById('reviewMessage').textContent = 'Пожалуйста, введите отзыв!';
    }
    else {
        document.getElementById('reviewMessage').textContent = 'Отзыв успешно отправлен!';
    document.getElementById('reviewInput').value = ''; // Очищаем поле
    const response =  fetch('http://localhost:8000/reviews', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ review: reviewInput }),
        });
    }
});
