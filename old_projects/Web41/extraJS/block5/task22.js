const pricePerKg = parseFloat(prompt("Введите стоимость 1 кг конфет (в рублях):"));

if (isNaN(pricePerKg) || pricePerKg <= 0) {
    console.log("Некорректный ввод. Пожалуйста, введите положительное число.");
} else {
    console.log("Вес (г) | Стоимость (руб.)");
    console.log("-------------------------");

    for (let weight = 100; weight <= 2000; weight += 100) {
        const cost = (weight / 1000) * pricePerKg; 
        console.log(`${weight}      | ${cost.toFixed(2)}`); 
    }
}