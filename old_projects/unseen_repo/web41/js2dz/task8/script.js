document.getElementById('circleSquareButton').addEventListener('click', function() {
    const circumference = Number(document.getElementById('circleInput').value);
    const perimeter = Number(document.getElementById('squareInput').value);
    const circleSquareResult = document.getElementById('circleSquareResult');

    const radius = circumference / (2 * Math.PI);
    const squareSide = perimeter / 4;

    circleSquareResult.textContent = radius <= squareSide / 2 ? "Окружность помещается в квадрат." : "Окружность не помещается в квадрат.";
});
