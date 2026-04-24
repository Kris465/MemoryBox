document.getElementById('circleSquareButton').addEventListener('click', function() {
    const circle = Number(document.getElementById('circleInput').value);
    const square = Number(document.getElementById('squareInput').value);
    const circleSquareResult = document.getElementById('circleSquareResult');

    const diametr = circle / Math.PI; 
    const side = square / 4;
    
    circleSquareResult.textContent = diametr <= side ? 'окружность помещается в квадрат': 'окружность не помещается в квадрат';
});