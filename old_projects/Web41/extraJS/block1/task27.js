const prompt = require('prompt-sync')();

function distance(height) {
    const R = 6350; 

    let distance = Math.sqrt(2 * height * R); 

    return distance;
}

const height = parseFloat(prompt("Введите высоту над уровнем моря (в км): "));

if (isNaN(height) || height < 0) {
  console.log("Пожалуйста, введите положительное число для высоты.");
} else {

  const horizonDistance = distance(height);
  console.log(`Расстояние до линии горизонта от высоты ${height} км: ${horizonDistance.toFixed(2)} км`);
}