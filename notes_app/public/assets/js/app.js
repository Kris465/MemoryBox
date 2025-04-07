// Подтверждение удаления (дублирует onclick для надёжности)
document.querySelectorAll('.btn-delete').forEach(btn => {
    btn.addEventListener('click', (e) => {
        if (!confirm('Удалить заметку?')) {
            e.preventDefault();
        }
    });
});

// Анимация загрузки
document.addEventListener('DOMContentLoaded', () => {
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.3s';
        document.body.style.opacity = '1';
    }, 100);
});