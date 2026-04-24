const prompt = require('prompt-sync')();
function getTrafficLightColor(t) {

    const period = 8;

    
    const timeInCycle = t % period;

  
    if (timeInCycle < 3) {
        return "Зеленый";
    } else if (timeInCycle < 5) {
        return "Красный";
    } else {
        return "Зеленый";
    }
}


try {
    let t = parseFloat(prompt("Введите время в минутах, прошедшее с начала часа (t):"));

    if (!isNaN(t) && t >= 0) {
        const color = getTrafficLightColor(t);
        console.log(`Сигнал светофора для пешеходов: ${color}`);
    } else {
        throw new Error("Пожалуйста, введите корректное неотрицательное вещественное число.");
    }
} catch (error) {
    console.error("Произошла ошибка:", error.message);
}