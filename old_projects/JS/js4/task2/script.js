function showError(x) {
    alert(`Error ${x} occurred!`);
}

document.getElementById("errorButton").addEventListener("click", function() {
    const errorText = document.getElementById("errorInput").value;
    showError(errorText);
});
