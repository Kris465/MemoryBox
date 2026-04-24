function sign(x) {
    return x > 0 ? 1 : x < 0 ? -1 : 0;
}

document.getElementById("checkSignButton").addEventListener("click", function() {
    const number = parseFloat(document.getElementById("numberInput").value);
    const result = sign(number);
    document.getElementById("result").textContent = result;
});
