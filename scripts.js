window.addEventListener("scroll", () => {
const image = document.querySelector(".hero-image");
const scrollY = window.scrollY;
image.style.transform = `translateY(${scrollY * 0.3}px) scale(1.05)`;
});
