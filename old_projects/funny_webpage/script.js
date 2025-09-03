function changeDescription() {
    var description = prompt("Введите новое описание персонажа:");
    if (description !== null) {
        document.getElementById("description").textContent = description;
    }
}
