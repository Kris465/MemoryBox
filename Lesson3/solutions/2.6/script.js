function validateForm() {
    const x = parseInt(document.getElementById('x').value);
    const y = parseInt(document.getElementById('y').value);
    const shape = document.getElementById('shape').value;

    const canvasWidth = 800;
    const canvasHeight = 600;

    if (shape === 'circle') {
        if (x < 0 || x > canvasWidth || y < 0 || y > canvasHeight) {
            alert("Круг выходит за пределы экрана!");
            return false;
        }
    } else if (shape === 'square') {
        if (x < 0 || x > canvasWidth - 50 || y < 0 || y > canvasHeight - 50) {
            alert("Квадрат выходит за пределы экрана!");
            return false;
        }
    } else if (shape === 'triangle') {
        if (x < 0 || x > canvasWidth - 50 || y < 0 || y > canvasHeight) {
            alert("Треугольник выходит за пределы экрана!");
            return false;
        }
    }

    const formData = new FormData(document.getElementById('shapeForm'));

    fetch('draw.php', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('canvas').innerHTML = data;
        document.getElementById('message').innerHTML = "";
    })
    .catch(error => console.error('Ошибка:', error));

    return false;
}
