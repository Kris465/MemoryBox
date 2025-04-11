document.addEventListener('DOMContentLoaded', function() {
    const togglePassword = document.querySelector('.toggle-password');
    const passwordInput = document.getElementById('password');
    
    if (togglePassword && passwordInput) {
        togglePassword.addEventListener('click', function() {
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            
            const icon = this.querySelector('i');
            icon.classList.toggle('fa-eye');
            icon.classList.toggle('fa-eye-slash');
        });
    }

    // Form validation
    const loginForm = document.querySelector('.admin-login-form');
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            const email = document.getElementById('email').value.trim();
            const password = document.getElementById('password').value.trim();
            let isValid = true;
            
            // Clear previous errors
            document.querySelectorAll('.error-message').forEach(el => el.remove());
            
            // Email validation
            if (!email) {
                showError('email', 'Пожалуйста, введите email');
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                showError('email', 'Пожалуйста, введите корректный email');
                isValid = false;
            }
            
            // Password validation
            if (!password) {
                showError('password', 'Пожалуйста, введите пароль');
                isValid = false;
            }
            
            // Prevent submit only if invalid
            if (!isValid) {
                e.preventDefault();
            }
            // If valid - form will submit normally
        });
    }
    
    function showError(fieldId, message) {
        const field = document.getElementById(fieldId);
        if (!field) return;
        
        const error = document.createElement('div');
        error.className = 'error-message text-danger mt-1 small';
        error.textContent = message;
        
        field.parentNode.appendChild(error);
    }
});