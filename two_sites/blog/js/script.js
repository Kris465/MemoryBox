class Single {
    constructor() {
        this.preloader = document.getElementById('preloader');
        this.header = document.getElementById('header');
        this.themeToggle = document.getElementById('themeToggle');
        this.themeIcon = this.themeToggle ? this.themeToggle.querySelector('i') : null;
        this.themeTransitionOverlay = document.getElementById('theme-transition-overlay');
        this.heroVideo = document.getElementById('heroVideo');
        this.heroPlaceholder = document.getElementById('heroPlaceholder');
        this.exploreBtn = document.getElementById('explore-btn');
        this.postsGrid = document.getElementById('postsGrid');
        this.loadMoreBtn = document.getElementById('load-more-btn');
        this.loadMoreButtonContainer = document.getElementById('load-more-container');
        this.loadingIndicator = document.getElementById('loadingIndicator');
        this.backToTopBtn = document.getElementById('back-to-top');
        this.subscribeBtn = document.getElementById('subscribe-btn');
        this.emailSubscribeInput = document.getElementById('email-subscribe');
        this.notificationModal = document.getElementById('notification-modal');
        this.closeModalBtn = document.getElementById('close-modal-btn');
        this.modalMessage = document.getElementById('modal-message');
        this.adminPanel = document.getElementById('admin-panel');
        this.sectionTitles = document.querySelectorAll('.section-title');
        this.html = document.documentElement;

        this.addNewsBtn = document.getElementById('add-news-btn');
        this.editNewsBtn = document.getElementById('edit-news-btn');
        this.deleteNewsBtn = document.getElementById('delete-news-btn');
        this.viewUsersBtn = document.getElementById('view-users-btn');
        this.configureSiteBtn = document.getElementById('configure-site-btn');

        this.addNewsModal = document.getElementById('add-news-modal');
        this.addNewsForm = document.getElementById('add-news-form');
        this.newsTitleInput = document.getElementById('news-title');
        this.newsCategoryInput = document.getElementById('news-category');
        this.newsImageInput = document.getElementById('news-image');
        this.newsExcerptInput = document.getElementById('news-excerpt');
        this.submitNewsBtn = document.getElementById('submit-news-btn');
        this.closeAddNewsModalBtn = document.getElementById('close-add-news-modal-btn');

        this.currentArticleCount = 0;
        this.articlesPerLoad = 6;
        this.postsPerScroll = 3;
        this.isLoading = false;
        this.infiniteScrollEnabled = false;

        this.allPossiblePosts = [
            { image: 'https://images.unsplash.com/photo-1546187948-aa13778007a3?auto=format&fit=crop&w=600&q=80', category: 'Охота', title: 'Скорость и тактика: Гепарды на пике своей формы', text: 'Узнайте о невероятных охотничьих стратегиях гепардов, их адаптациях к скорости и о том, как они сохраняют звание самых быстрых наземных животных.' },
            { image: 'https://images.unsplash.com/photo-1596207166567-2d4e3e3b7b2b?auto=format&fit=crop&w=600&q=80', category: 'Интеллект', title: 'Тайны разума осьминогов: Морские гении', text: 'Новые исследования показывают удивительный интеллект осьминогов, их способность к решению сложных задач и использование инструментов.' },
            { image: 'https://images.unsplash.com/photo-1560592966-26797a7e8705?auto=format&fit=crop&w=600&q=80', category: 'Миграция', title: 'Грандиозное путешествие бабочек-монархов', text: 'Ежегодная миграция бабочек-монархов остается одним из самых впечатляющих природных феноменов. Узнайте, как они преодолевают тысячи километров.' },
            { image: 'https://images.unsplash.com/photo-1517404179374-bd9a3d4d420b?auto=format&fit=crop&w=600&q=80', category: 'Поведение', title: 'Удивительные привычки медведей гризли', text: 'Познакомьтесь с образом жизни медведей гризли, их диетой, социальными структурами и уникальными способами адаптации к окружающей среде.' },
            { image: 'https://images.unsplash.com/photo-1549417277-2280d0d81b3b?auto=format&fit=crop&w=600&q=80', category: 'Природа', title: 'Гармония в воздухе: Птицы как индикаторы здоровья экосистем', text: 'Изучение поведения и численности птиц помогает ученым оценивать здоровье нашей планеты. Узнайте, как пернатые друзья сигнализируют об изменениях.' },
            { image: 'https://images.unsplash.com/photo-1510414986872-b80894a8d052?auto=format&fit=crop&w=600&q=80', category: 'Океан', title: 'Неизведанные глубины: Жизнь в самых темных уголках океана', text: 'Погрузитесь в тайны глубоководных существ, их удивительные формы жизни и адаптации к экстремальным условиям, о которых мы только начинаем узнавать.' },
            { image: 'https://images.unsplash.com/photo-1547476902-1279f71c4c36?auto=format&fit=crop&w=600&q=80', category: 'Поведение', title: 'Почему лисы такие хитрые: Новые исследования', text: 'Ученые изучают сложное поведение лис и их адаптации, позволяющие им выживать в самых разных условиях. Откройте для себя их удивительные стратегии.' },
            { image: 'https://images.unsplash.com/photo-1589182333068-d050519a16f2?auto=format&fit=crop&w=600&q=80', category: 'Сохранение', title: 'Битва за носорогов: Успехи в борьбе с браконьерством', text: 'Узнайте о героических усилиях рейнджеров и природоохранных организаций, которые добиваются успехов в защите носорогов от браконьеров.' },
            { image: 'https://images.unsplash.com/photo-1579309600000-0e1d5e5e5f5e?ixlib=rb-1.2.1&auto=format&fit=crop&w=600&q=80', category: 'Исчезающие Виды', title: 'Красные панды: Секреты выживания и новые угрозы', text: 'Красные панды сталкиваются с новыми угрозами в дикой природе, но усилия по их сохранению дают надежду на выживание этого уникального вида.' },
            { image: 'https://images.unsplash.com/photo-1519098733245-c89b88c1c4e7?auto=format&fit=crop&w=600&q=80', category: 'Хищники', title: 'Ирбис: Призраки гор и их уникальные адаптации', text: 'Откройте для себя жизнь неуловимого снежного барса, обитающего в суровых горных ландшафтах, и его удивительные способности выживать в холоде.' },
            { image: 'https://images.unsplash.com/photo-1540573133999-52e03b6038a0?auto=format&fit=crop&w=600&q=80', category: 'Рептилии', title: 'Мир змей: Факты, которые вас удивят', text: 'Развейте мифы о змеях и узнайте о их важнейшей роли в экосистеме, их уникальных видах и поведении, которое шокирует.' },
            { image: 'https://images.unsplash.com/photo-1542475080-b2867cf840f4?auto=format&fit=crop&w=600&q=80', category: 'Биология', title: 'Фотосинтезирующие животные: Невероятные симбиозы', text: 'Некоторые животные используют фотосинтез для выживания, вступая в симбиоз с водорослями. Узнайте о самых необычных формах жизни.' }
        ];
        this.shuffledPosts = [...this.allPossiblePosts];
        this.shuffleArray(this.shuffledPosts);
    }

    init() {
        this.bindEventListeners();
        this.applySavedTheme();
        this.loadHeroVideo();
        this.loadArticles(this.articlesPerLoad);
        window.dispatchEvent(new Event('scroll'));
        this.hidePreloader();
    }

    bindEventListeners() {
        if (this.themeToggle) {
            this.themeToggle.addEventListener('click', (event) => this.toggleTheme(event));
        }
        if (this.exploreBtn) {
            this.exploreBtn.addEventListener('click', (e) => this.scrollToSection(e, 'news'));
        }
        if (this.loadMoreBtn) {
            this.loadMoreBtn.addEventListener('click', () => this.handleLoadMore());
        }
        window.addEventListener('scroll', () => this.handleScroll());
        if (this.backToTopBtn) {
            this.backToTopBtn.addEventListener('click', () => this.scrollToTop());
        }
        if (this.subscribeBtn) {
            this.subscribeBtn.addEventListener('click', () => this.handleSubscribe());
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

        if (this.addNewsBtn) {
            this.addNewsBtn.addEventListener('click', () => this.showModal(this.addNewsModal));
        }
        if (this.editNewsBtn) {
            this.editNewsBtn.addEventListener('click', () => this.adminEditNews());
        }
        if (this.deleteNewsBtn) {
            this.deleteNewsBtn.addEventListener('click', () => this.adminDeleteNews());
        }
        if (this.viewUsersBtn) {
            this.viewUsersBtn.addEventListener('click', () => this.adminViewUsers());
        }
        if (this.configureSiteBtn) {
            this.configureSiteBtn.addEventListener('click', () => this.adminConfigureSite());
        }

        if (this.addNewsForm) {
            this.addNewsForm.addEventListener('submit', (e) => this.handleAddNewsSubmit(e));
        }
        if (this.closeAddNewsModalBtn) {
            this.closeAddNewsModalBtn.addEventListener('click', () => this.hideModal(this.addNewsModal));
        }
        if (this.addNewsModal) {
            this.addNewsModal.addEventListener('click', (e) => {
                if (e.target === this.addNewsModal) {
                    this.hideModal(this.addNewsModal);
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

        this.sectionTitleObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate-in');
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.2 });
        this.sectionTitles.forEach(title => {
            this.sectionTitleObserver.observe(title);
        });
    }

    hidePreloader() {
        if (this.preloader) {
            this.preloader.style.opacity = '0';
            setTimeout(() => {
                this.preloader.style.display = 'none';
                if (this.header) {
                    this.header.classList.remove('hidden');
                }
            }, 500);
        }
    }

    loadHeroVideo() {
        if (this.heroVideo && this.heroPlaceholder) {
            this.heroVideo.oncanplaythrough = () => {
                this.heroPlaceholder.style.opacity = '0';
                setTimeout(() => {
                    this.heroPlaceholder.style.display = 'none';
                    this.heroVideo.style.display = 'block';
                    this.heroVideo.play().catch(e => console.log('Autoplay prevented:', e));
                }, 500);
            };
            this.heroVideo.load();
            this.heroVideo.onerror = () => {
                console.error('Failed to load hero video, using placeholder.');
                this.heroPlaceholder.style.display = 'block';
                this.heroVideo.style.display = 'none';
            };
        }
    }

    toggleTheme(event) {
        let currentTheme = this.html.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
        this.html.setAttribute('data-theme', newTheme);
        localStorage.setItem('theme', newTheme);

        if (this.themeIcon) {
            this.themeIcon.classList.remove(newTheme === 'dark' ? 'fa-sun' : 'fa-moon');
            this.themeIcon.classList.add(newTheme === 'dark' ? 'fa-moon' : 'fa-sun');
        }

        const rect = this.themeToggle.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        this.themeTransitionOverlay.classList.remove('hidden');
        this.themeTransitionOverlay.style.left = `${rect.left + x}px`;
        this.themeTransitionOverlay.style.top = `${rect.top + y}px`;

        const rippleColorStart = getComputedStyle(this.html).getPropertyValue(`--ripple-start-${currentTheme}`).trim();
        const rippleColorEnd = getComputedStyle(this.html).getPropertyValue(`--ripple-end-${currentTheme}`).trim();

        this.themeTransitionOverlay.style.background = `radial-gradient(circle at ${x}px ${y}px, ${rippleColorStart} 0%, ${rippleColorEnd} 100%)`;
        this.themeTransitionOverlay.style.transform = 'scale(0)';
        this.themeTransitionOverlay.style.opacity = '1';

        void this.themeTransitionOverlay.offsetWidth;

        const maxDim = Math.max(window.innerWidth, window.innerHeight);
        const scaleFactor = maxDim / Math.min(rect.width, rect.height) * 1.5;
        this.themeTransitionOverlay.style.transform = `scale(${scaleFactor})`;
        this.themeTransitionOverlay.style.opacity = '0';

        setTimeout(() => {
            this.themeTransitionOverlay.classList.add('hidden');
            this.themeTransitionOverlay.style.transform = 'scale(0)';
            this.themeTransitionOverlay.style.transition = 'none';
        }, 500);
    }

    applySavedTheme() {
        const savedTheme = localStorage.getItem('theme') || (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
        this.html.setAttribute('data-theme', savedTheme);
        if (this.themeIcon) {
            this.themeIcon.classList.remove(savedTheme === 'dark' ? 'fa-moon' : 'fa-sun');
            this.themeIcon.classList.add(savedTheme === 'dark' ? 'fa-sun' : 'fa-moon');
        }
    }

    scrollToSection(e, sectionId) {
        e.preventDefault();
        const section = document.getElementById(sectionId);
        if (section) {
            section.scrollIntoView({ behavior: 'smooth' });
        }
    }

    createPostCardHtml(post) {
        const currentTheme = this.html.getAttribute('data-theme');
        const textColor = currentTheme === 'dark' ? 'var(--color-text-dark)' : 'var(--color-text-light)';
        const textDimColor = currentTheme === 'dark' ? 'var(--color-text-dark-dim)' : 'var(--color-text-light-dim)';
        const primaryColor = currentTheme === 'dark' ? 'var(--color-primary-dark)' : 'var(--color-primary-light)';
        const accentColor = currentTheme === 'dark' ? 'var(--color-accent-dark)' : 'var(--color-accent-light)';

        return `
            <article class="post-card article-card" style="opacity: 0; transform: translateY(20px);">
                <img src="${post.image}" loading="lazy" onerror="this.onerror=null;this.src='https://placehold.co/600x400/CCCCCC/333333?text=Image+Missing';" alt="${post.title}" class="w-full h-48 object-cover rounded-xl mb-5 border-green-300">
                <div class="p-6">
                    <span class="inline-block text-white py-1 px-4 rounded-full text-xs font-bold mb-3 uppercase tracking-wider" style="background-color: ${primaryColor};">${post.category}</span>
                    <h3 class="font-['Playfair_Display'] text-2xl font-bold mb-3" style="color: ${textColor};">${post.title}</h3>
                    <p class="mb-4 line-clamp-3" style="color: ${textDimColor};">${post.text}</p>
                    <a href="#" class="inline-flex items-center gap-2 font-semibold text-md hover:underline transition-colors duration-200" style="color: ${accentColor};">
                        Читать далее <i class="fas fa-arrow-right"></i>
                    </a>
                </div>
            </article>
        `;
    }

    shuffleArray(array) {
        for (let i = array.length - 1; i > 0; i--) {
            const j = Math.floor(Math.random() * (i + 1));
            [array[i], array[j]] = [array[j], array[i]];
        }
    }

    loadArticles(count) {
        if (!this.postsGrid) return 0;

        const fragment = document.createDocumentFragment();
        let postsAdded = 0;

        if (this.currentArticleCount === 0 && this.postsGrid.children.length > 0) {
            this.postsGrid.innerHTML = '';
        }

        const startIndex = this.postsGrid.children.length;
        const endIndex = Math.min(startIndex + count, this.shuffledPosts.length);

        for (let i = startIndex; i < endIndex; i++) {
            const post = this.shuffledPosts[i];
            const div = document.createElement('div');
            div.innerHTML = this.createPostCardHtml(post).trim();
            fragment.appendChild(div.firstChild);
            postsAdded++;
        }
        this.postsGrid.appendChild(fragment);

        const newCards = Array.from(this.postsGrid.children).slice(-postsAdded);
        newCards.forEach((card, index) => {
            card.style.animationDelay = `${index * 0.1}s`;
            card.style.animation = 'fadeInUp 0.8s ease forwards';
        });

        this.currentArticleCount = this.postsGrid.children.length;

        if (this.loadMoreButtonContainer) {
            if (this.currentArticleCount >= this.shuffledPosts.length) {
                this.loadMoreButtonContainer.classList.add('hidden');
                if (this.loadingIndicator) {
                    this.loadingIndicator.classList.add('hidden');
                }
            } else {
                this.loadMoreButtonContainer.classList.remove('hidden');
            }
        }
        return postsAdded;
    }

    handleLoadMore() {
        if (this.isLoading || this.currentArticleCount >= this.shuffledPosts.length) {
            return;
        }

        this.isLoading = true;
        if (this.loadingIndicator) this.loadingIndicator.classList.remove('hidden');
        if (this.loadMoreButtonContainer) this.loadMoreButtonContainer.classList.add('hidden');

        setTimeout(() => {
            const addedCount = this.loadArticles(this.postsPerScroll);
            this.isLoading = false;
            if (this.loadingIndicator) this.loadingIndicator.classList.add('hidden');

            if (addedCount === 0 && this.currentArticleCount >= this.shuffledPosts.length) {
                console.log("Все уникальные публикации загружены.");
                if (this.loadMoreButtonContainer) this.loadMoreButtonContainer.classList.add('hidden');
            } else if (this.currentArticleCount < this.shuffledPosts.length) {
                if (this.loadMoreButtonContainer) this.loadMoreButtonContainer.classList.remove('hidden');
            }
        }, 1000);
    }

    handleScroll() {
        const { scrollTop, scrollHeight, clientHeight } = document.documentElement;

        if (scrollTop > 50) {
            this.header.classList.add('header-scrolled');
        } else {
            this.header.classList.remove('header-scrolled');
        }

        if (scrollTop > 300) {
            this.backToTopBtn.classList.add('show');
        } else {
            this.backToTopBtn.classList.remove('show');
        }

        if (this.infiniteScrollEnabled && scrollTop + clientHeight > scrollHeight - 800 && !this.isLoading && this.currentArticleCount < this.shuffledPosts.length) {
            this.handleLoadMore();
        }

        document.querySelectorAll('#subscribe, #about, #contact, #admin-panel').forEach(element => {
            const rect = element.getBoundingClientRect();
            if (rect.top < window.innerHeight * 0.85 && rect.bottom > 0 && element.style.animation === '') {
                element.style.animation = 'fadeSlideIn 1s ease forwards';
            }
        });
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
            void modalElement.offsetWidth;
            const modalContent = modalElement.querySelector('.modal-content');
            if (modalContent) {
                modalContent.classList.remove('scale-0');
            }
            document.body.style.overflow = 'hidden';
        }
    }

    hideModal(modalElement) {
        if (modalElement) {
            const modalContent = modalElement.querySelector('.modal-content');
            if (modalContent) {
                modalContent.classList.add('scale-0');
            }
            setTimeout(() => {
                modalElement.classList.add('hidden');
                document.body.style.overflow = '';
            }, 300);
        }
    }

    handleSubscribe() {
        const email = this.emailSubscribeInput ? this.emailSubscribeInput.value : '';
        if (email && email.includes('@') && email.includes('.')) {
            console.log(`Подписка на email: ${email}`);
            this.showModal(this.notificationModal);
            if (this.modalMessage) {
                this.modalMessage.textContent = `Вы успешно подписались на рассылку на ${email}! Теперь вы будете получать самые горячие и эксклюзивные новости о животных прямо на вашу почту.`;
            }
            if (this.emailSubscribeInput) {
                this.emailSubscribeInput.value = '';
            }
        } else {
            this.showModal(this.notificationModal);
            if (this.modalMessage) {
                this.modalMessage.textContent = 'Пожалуйста, введите корректный адрес электронной почты для подписки.';
            }
            if (this.emailSubscribeInput) {
                this.emailSubscribeInput.classList.add('border-red-500', 'animate-pulse');
                setTimeout(() => {
                    this.emailSubscribeInput.classList.remove('border-red-500', 'animate-pulse');
                }, 1000);
            }
        }
    }

    handleAddNewsSubmit(e) {
        e.preventDefault();

        const title = this.newsTitleInput.value.trim();
        const category = this.newsCategoryInput.value.trim();
        const image = this.newsImageInput.value.trim();
        const excerpt = this.newsExcerptInput.value.trim();

        if (title && category && image && excerpt) {
            const newArticle = {
                image: image,
                category: category,
                title: title,
                text: excerpt
            };

            this.allPossiblePosts.unshift(newArticle);
            this.shuffledPosts.unshift(newArticle);

            this.addNewsForm.reset();

            this.hideModal(this.addNewsModal);

            this.currentArticleCount = 0;
            if (this.postsGrid) {
                this.postsGrid.innerHTML = '';
            }
            this.loadArticles(this.articlesPerLoad);

            this.showModal(this.notificationModal);
            if (this.modalMessage) {
                this.modalMessage.textContent = `Статья "${title}" успешно добавлена и отображена на сайте!`;
            }

            console.log('Admin: Добавлена новая статья:', newArticle);
        } else {
            this.showModal(this.notificationModal);
            if (this.modalMessage) {
                this.modalMessage.textContent = 'Пожалуйста, заполните все поля для добавления статьи.';
            }
        }
    }

    adminEditNews() {
        this.showModal(this.notificationModal);
        if (this.modalMessage) {
            this.modalMessage.textContent = 'Функционал "Редактировать Новость" находится в разработке. В реальном приложении здесь будет форма с выбранной статьей для изменения.';
        }
        console.log('Admin: Редактировать Новость');
    }

    adminDeleteNews() {
        this.showModal(this.notificationModal);
        if (this.modalMessage) {
            this.modalMessage.textContent = 'Функционал "Удалить Новость" находится в разработке. В реальном приложении здесь будет подтверждение удаления выбранной статьи.';
        }
        console.log('Admin: Удалить Новость');
    }

    adminViewUsers() {
        this.showModal(this.notificationModal);
        if (this.modalMessage) {
            this.modalMessage.textContent = 'Функционал "Просмотреть Пользователей" находится в разработке. Здесь будет отображаться список пользователей и их управление.';
        }
        console.log('Admin: Просмотреть Пользователей');
    }

    adminConfigureSite() {
        this.showModal(this.notificationModal);
        if (this.modalMessage) {
            this.modalMessage.textContent = 'Функционал "Настроить Сайт" находится в разработке. Здесь будут глобальные настройки сайта.';
        }
        console.log('Admin: Настроить Сайт');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const app = new Single();
    app.init();
});
