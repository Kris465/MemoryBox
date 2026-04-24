function checkPassword(x) {
    return x === "Step" || x === "Web" || x === "JavaScript";
}

document.getElementById("checkPasswordButton").addEventListener("click", function() {
    const password = document.getElementById("passwordInput").value;
    const isValid = checkPassword(password);
    document.getElementById("result").textContent = isValid ? "Пароль допустимый" : "Пароль недопустимый";
});
