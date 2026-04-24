function createHeaders(N) {
    const container = document.getElementById("headersContainer");
    container.innerHTML = "";
    for (let i = 1; i <= N; i++) {
        const header = document.createElement("h2");
        header.textContent = `Заголовок ${i}`;
        container.appendChild(header);
    }
}

document.getElementById("createHeadersButton").addEventListener("click", function() {
    const count = parseInt(document.getElementById("headerCount").value);
    if (!isNaN(count) && count > 0) {
        createHeaders(count);
    }
});
