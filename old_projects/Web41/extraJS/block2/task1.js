const prompt = require('prompt-sync')();

function centimetersToMeters(centimeters) {
    const meters = Math.floor(centimeters / 100);
    return meters;
}
  
const distanceInCentimeters = prompt("Введите колличество сантиметров : ");
const fullMeters = centimetersToMeters(distanceInCentimeters);
  
console.log(`В ${distanceInCentimeters} сантиметрах ${fullMeters} полных метров.`);

const anotherDistance = prompt("Введите введите количество меторов : ");
const metersInAnotherDistance = centimetersToMeters(anotherDistance);
console.log(`В ${anotherDistance} сантиметрах ${metersInAnotherDistance} полных метров.`);

