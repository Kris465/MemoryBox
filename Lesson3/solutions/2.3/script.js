document.addEventListener("DOMContentLoaded", function() {
    const container = document.getElementById("container");
    
    setTimeout(() => {
        container.style.opacity = "1";
        container.style.transform = "translateY(0)";
    }, 100);
});
