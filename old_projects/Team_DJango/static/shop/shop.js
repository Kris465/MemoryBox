
class ShopApp {
    constructor() {
        if (ShopApp.instance) {
            return ShopApp.instance;
        }
        ShopApp.instance = this;
        console.log('ShopApp: Инициализация магазина.');

        this.cartItems = [];
        this.bindEventListeners();
    }

    init() {
        console.log('ShopApp: Магазин запущен.');
    }

    bindEventListeners() {
        document.querySelectorAll('.buy-button').forEach(button => {
            button.addEventListener('click', (event) => this.addToCart(event));
        });

        const contactForm = document.querySelector(".contact-form");
        if (contactForm) {
            contactForm.addEventListener("submit", (event) => {
                event.preventDefault();
                const name = contactForm.querySelector('input[type="text"]').value;
                const email = contactForm.querySelector('input[type="email"]').value;
                const message = contactForm.querySelector('textarea').value;

                console.log("Сообщение отправлено:");
                console.log("Имя:", name);
                console.log("Почта:", email);
                console.log("Сообщение:", message);

                this.showCustomAlert("Ваше сообщение отправлено! Мы свяжемся с вами в ближайшее время.");
                contactForm.reset();
            });
        }
    }

    addToCart(event) {
        const productCard = event.target.closest('.product-card');
        const productName = productCard.querySelector('h3').textContent.split('<span')[0].trim();
        const productPrice = productCard.querySelector('.price').textContent;

        this.cartItems.push({ name: productName, price: productPrice });
        console.log(`ShopApp: Товар "${productName}" добавлен в корзину. Текущая корзина:`, this.cartItems);
        this.showCustomAlert(`"${productName}" добавлен в корзину!`);
    }

    showCustomAlert(message) {
        let alertModal = document.getElementById('shopCustomAlertModal');
        if (!alertModal) {
            alertModal = document.createElement('div');
            alertModal.id = 'shopCustomAlertModal';
            alertModal.className = 'fixed inset-0 bg-black bg-opacity-70 backdrop-blur-md flex items-center justify-center z-[1000] hidden';
            alertModal.innerHTML = `
                <div class="bg-white p-8 rounded-2xl shadow-xl max-w-sm w-full text-center transform scale-0 transition-transform duration-300">
                    <h3 class="text-3xl font-bold text-green-700 mb-4">Сообщение магазина</h3>
                    <p class="text-gray-700 mb-6" id="shopAlertMessage"></p>
                    <button class="bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-8 rounded-full text-lg shadow-md" onclick="shopAppInstance.hideCustomAlert()">
                        ОК
                    </button>
                </div>
            `;
            document.body.appendChild(alertModal);
        }

        const alertMessageEl = document.getElementById('shopCustomAlertModal').querySelector('#shopAlertMessage');
        alertMessageEl.textContent = message;
        alertModal.classList.remove('hidden');
        setTimeout(() => alertModal.querySelector('div').classList.add('active'), 10);
    }

    hideCustomAlert() {
        const alertModal = document.getElementById('shopCustomAlertModal');
        if (alertModal) {
            alertModal.querySelector('div').classList.remove('active');
            alertModal.querySelector('div').addEventListener('transitionend', () => {
                if (!alertModal.querySelector('div').classList.contains('active')) {
                    alertModal.classList.add('hidden');
                }
            }, { once: true });
        }
    }
}

document.addEventListener('DOMContentLoaded', () => {
    window.shopAppInstance = new ShopApp();
    shopAppInstance.init();
});
