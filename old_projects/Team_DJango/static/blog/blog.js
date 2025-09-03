
class BlogApp {
    constructor() {
        if (BlogApp.instance) {
            return BlogApp.instance;
        }
        BlogApp.instance = this;

        this.preloader = document.getElementById('preloader');
        this.header = document.getElementById('main-header');
        this.themeToggle = document.getElementById('themeToggle');
        this.themeIcon = this.themeToggle ? this.themeToggle.querySelector('i') : null;
        this.themeTransitionOverlay = document.getElementById('theme-transition-overlay');
        this.postsGrid = document.getElementById('postsGrid');
        this.loadMoreBtn = document.getElementById('load-more-btn');
        this.loadMoreButtonContainer = document.getElementById('load-more-container');
        this.loadingIndicator = document.getElementById('loadingIndicator');
        this.backToTopBtn = document.getElementById('back-to-top');
        this.notificationModal = document.getElementById('notification-modal');
        this.closeModalBtn = document.getElementById('close-modal-btn');
        this.html = document.documentElement;

        this.articlesPerLoad = 6;
        this.isLoading = false;
        this.infiniteScrollEnabled = false;
    }

    init() {
        if (this.preloader) {
            this.preloader.style.display = 'flex';
            this.preloader.style.opacity = '1';
        }

        this.bindEventListeners();
        this.applySavedTheme();
        
        setTimeout(() => {
            window.dispatchEvent(new Event('scroll'));
            this.hidePreloader();
        }, 500); 

        if (this.loadMoreBtn && this.loadMoreBtn.dataset.nextPage) {
            this.loadMoreButtonContainer.classList.remove('hidden');
        } else if (this.loadMoreButtonContainer) {
            this.loadMoreButtonContainer.classList.add('hidden');
        }
    }

    bindEventListeners() {
        if (this.themeToggle) {
            this.themeToggle.addEventListener('click', (event) => this.toggleTheme(event));
        }
        if (this.loadMoreBtn) {
            this.loadMoreBtn.addEventListener('click', () => this.handleLoadMore());
        }
        window.addEventListener('scroll', () => this.handleScroll());
        if (this.backToTopBtn) {
            this.backToTopBtn.addEventListener('click', () => this.scrollToTop());
        }
        if (this.closeModalBtn) {
            this.closeModalBtn.addEventListener('click', () => this.hideModal(this.notificationModal));
        }
        if (this.notificationModal) {
            this.notificationModal.addEventListener('click', (e) => {
                if (e.target === this.notificationModal) {
                    this.hideModal(this.notificationModal);
                }
            });
        }
        
        document.querySelectorAll('.btn-effect').forEach(button => {
            button.addEventListener('mousedown', () => {
                button.classList.add('shadow-inner', 'bg-opacity-90');
            });
            button.addEventListener('mouseup', () => {
                button.classList.remove('shadow-inner', 'bg-opacity-90');
            });
            button.addEventListener('mouseleave', () => {
                button.classList.remove('shadow-inner', 'bg-opacity-90');
            });
        });
    }

    hidePreloader() {
        if (this.preloader) {
            this.preloader.style.opacity = '0';
            this.preloader.addEventListener('transitionend', () => {
                this.preloader.style.display = 'none';
                if (this.header) {
                    this.header.classList.remove('hidden');
                }
            }, { once: true });
        }
    }

    toggleTheme(event) {
        event.preventDefault(); 
        const isDark = this.html.getAttribute('data-theme') === 'dark';
        this.showThemeTransitionOverlay(!isDark); 

        setTimeout(() => {
            if (isDark) {
                this.html.setAttribute('data-theme', 'light');
                if (this.themeIcon) this.themeIcon.className = 'fas fa-moon';
            } else {
                this.html.setAttribute('data-theme', 'dark');
                if (this.themeIcon) this.themeIcon.className = 'fas fa-sun';
            }
            localStorage.setItem('theme', this.html.getAttribute('data-theme'));
            this.hideThemeTransitionOverlay(); 
        }, 300); 
    }

    applySavedTheme() {
        const savedTheme = localStorage.getItem('theme') || 'light';
        this.html.setAttribute('data-theme', savedTheme);
        if (this.themeIcon) {
            this.themeIcon.className = savedTheme === 'dark' ? 'fas fa-sun' : 'fas fa-moon';
        }
    }

    showThemeTransitionOverlay(isDarkToLight) {
        if (this.themeTransitionOverlay) {
            this.themeTransitionOverlay.style.backgroundColor = isDarkToLight ? 'white' : '#1a202c'; 
            this.themeTransitionOverlay.classList.remove('hidden');
            this.themeTransitionOverlay.style.opacity = '1';
        }
    }

    hideThemeTransitionOverlay() {
        if (this.themeTransitionOverlay) {
            this.themeTransitionOverlay.style.opacity = '0';
            this.themeTransitionOverlay.addEventListener('transitionend', () => {
                if (!this.themeTransitionOverlay.classList.contains('active')) { 
                    this.themeTransitionOverlay.classList.add('hidden');
                }
            }, { once: true });
        }
    }

    handleLoadMore() {
        const nextPage = this.loadMoreBtn.dataset.nextPage;
        if (!nextPage || this.isLoading) return;

        this.isLoading = true;
        this.loadingIndicator.classList.remove('hidden');
        if (this.loadMoreButtonContainer) {
            this.loadMoreButtonContainer.classList.add('hidden');
        }

        fetch(`?page=${nextPage}`, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => response.text())
        .then(html => {
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = html;
            const newPostsHtml = tempDiv.querySelector('#postsGrid').innerHTML;
            this.postsGrid.insertAdjacentHTML('beforeend', newPostsHtml);

            const newLoadMoreBtn = tempDiv.querySelector('#load-more-btn');
            if (newLoadMoreBtn) {
                this.loadMoreBtn.dataset.nextPage = newLoadMoreBtn.dataset.nextPage;
                if (!this.infiniteScrollEnabled) {
                     this.loadMoreButtonContainer.classList.remove('hidden');
                }
            } else {
                if (this.loadMoreButtonContainer) {
                    this.loadMoreButtonContainer.classList.add('hidden');
                }
            }
        })
        .catch(error => console.error('Ошибка загрузки статей:', error))
        .finally(() => {
            this.loadingIndicator.classList.add('hidden');
            this.isLoading = false;
        });
    }

    handleScroll() {
        const scrollY = window.scrollY || document.documentElement.scrollTop;

        if (this.header) {
            if (scrollY > 50) { 
                this.header.classList.add('header-scrolled'); 
            } else {
                this.header.classList.remove('header-scrolled');
            }
        }

        if (this.backToTopBtn) {
            if (scrollY > 300) { 
                this.backToTopBtn.classList.remove('opacity-0', 'invisible');
                this.backToTopBtn.classList.add('opacity-100', 'visible');
            } else {
                this.backToTopBtn.classList.remove('opacity-100', 'visible');
                this.backToTopBtn.classList.add('opacity-0', 'invisible');
            }
        }

        if (this.infiniteScrollEnabled && !this.isLoading &&
            (window.innerHeight + window.scrollY) >= (document.body.offsetHeight - 200) &&
            this.loadMoreBtn && this.loadMoreBtn.dataset.nextPage) { 
            this.handleLoadMore();
        }
    }

    scrollToTop() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    }

    showModal(modalElement) {
        if (modalElement) {
            modalElement.classList.remove('hidden');
            setTimeout(() => modalElement.classList.add('active'), 10); 
        }
    }

    hideModal(modalElement) {
        if (modalElement) {
            modalElement.classList.remove('active');
            modalElement.addEventListener('transitionend', () => {
                if (!modalElement.classList.contains('active')) { 
                    modalElement.classList.add('hidden');
                }
            }, { once: true });
        }
    }

    showCustomAlert(message) {
        const tempModalMessageEl = this.notificationModal.querySelector('p');
        const originalMessage = tempModalMessageEl.textContent;
        const originalTitle = this.notificationModal.querySelector('h3').textContent;

        this.notificationModal.querySelector('h3').textContent = 'Внимание!';
        tempModalMessageEl.textContent = message;
        this.showModal(this.notificationModal);

        this.notificationModal.querySelector('#close-modal-btn').onclick = () => {
            this.hideModal(this.notificationModal);
            this.notificationModal.querySelector('h3').textContent = originalTitle;
            tempModalMessageEl.textContent = originalMessage;
        };
    }

    getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
                
            }
        }
        return cookieValue;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const blogAppInstance = new BlogApp();
    blogAppInstance.init();
});
