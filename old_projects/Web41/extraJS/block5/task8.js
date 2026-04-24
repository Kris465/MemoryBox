const poundsToGrams = 453; 
const gramsToKilograms = 1000;

console.log("Фунты\tКилограммы");
for (let pounds = 1; pounds <= 10; pounds++) {
    const grams = pounds * poundsToGrams;
    const kilograms = (grams / gramsToKilograms).toFixed(3); 
    console.log(`${pounds}\t${kilograms}`);
}