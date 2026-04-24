document.addEventListener('DOMContentLoaded', function() {
    const validPassword = ['step', 'web', 'javascript'];
    let password = prompt('введите пароль: ');

    if (validPassword.includes(password)) {
        alert('подтвержденно')
    } else {
        alert('отклонено')
    }
} );