
const pricePerKg = parseFloat(prompt("Введите стоимость 1 кг сыра (в рублях):"));

if (isNaN(pricePerKg) || pricePerKg <= 0) {
    console.log("Пожалуйста, введите корректную стоимость.");
} else {
    console.log("Таблица стоимости сыра:");
    console.log("-------------------------");
    console.log("Вес (г)\t|\tСтоимость (руб.)");
    console.log("-------------------------");


    for (let weight = 50; weight <= 1000; weight += 50) {
        const cost = (weight / 1000) * pricePerKg; 
        console.log(`${weight}\t|\t${cost.toFixed(2)}`);
    }
}