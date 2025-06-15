
document.addEventListener('DOMContentLoaded', function() {
    const themeToggle = document.getElementById('themeToggle');
    const themeIcon = themeToggle ? themeToggle.querySelector('i') : null;
    const html = document.documentElement;
    const transitionOverlay = document.getElementById('theme-transition-overlay');

    function applySavedTheme() {
        const savedTheme = localStorage.getItem('theme') || 'light';
        html.setAttribute('data-theme', savedTheme);
        if (themeIcon) {
            themeIcon.className = savedTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
        }
    }

    function showThemeTransitionOverlay(isDarkToLight) {
        if (transitionOverlay) {
            transitionOverlay.style.backgroundColor = isDarkToLight ? 'white' : '#1a202c';
            transitionOverlay.classList.remove('hidden');
            transitionOverlay.style.transform = 'scale(0)';
            transitionOverlay.style.opacity = '1';
            requestAnimationFrame(() => {
                transitionOverlay.style.transform = 'scale(2)';
            });
        }
    }

    function hideThemeTransitionOverlay() {
        if (transitionOverlay) {
            transitionOverlay.style.opacity = '0';
            transitionOverlay.addEventListener('transitionend', () => {
                transitionOverlay.classList.add('hidden');
                transitionOverlay.style.transform = 'scale(0)';
            }, { once: true });
        }
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', (event) => {
            event.preventDefault();
            const isDark = html.getAttribute('data-theme') === 'dark';
            showThemeTransitionOverlay(!isDark);

            setTimeout(() => {
                if (isDark) {
                    html.setAttribute('data-theme', 'light');
                    if (themeIcon) themeIcon.className = 'fas fa-moon';
                } else {
                    html.setAttribute('data-theme', 'dark');
                    if (themeIcon) themeIcon.className = 'fas fa-sun';
                }
                localStorage.setItem('theme', html.getAttribute('data-theme'));
                hideThemeTransitionOverlay();
            }, 300);
        });
    }

    const mainHeader = document.getElementById('main-header');
    if (mainHeader) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) {
                mainHeader.classList.add('header-scrolled');
            } else {
                mainHeader.classList.remove('header-scrolled');
            }
        });
        window.dispatchEvent(new Event('scroll'));
    }

    applySavedTheme();
});
