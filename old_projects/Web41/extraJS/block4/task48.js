const prompt = require('prompt-sync')();


function areHeightsEqual(height1, height2, height3) {
    return height1 === height2 && height2 === height3;
}


try {
    let height1 = parseFloat(prompt("Введите рост первого человека (в метрах):"));
    let height2 = parseFloat(prompt("Введите рост второго человека (в метрах):"));
    let height3 = parseFloat(prompt("Введите рост третьего человека (в метрах):"));


    if (!isNaN(height1) && isFinite(height1) && height1 > 0 && 
        !isNaN(height2) && isFinite(height2) && height2 > 0 && 
        !isNaN(height3) && isFinite(height3) && height3 > 0) {
        
        const result = areHeightsEqual(height1, height2, height3);
        
        if (result) {
            console.log("Да, рост всех трех человек одинаков.");
        } else {
            console.log("Нет, рост не одинаков.");
        }
    } else {
        throw new Error("Пожалуйста, введите корректные положительные значения роста.");
    }
} catch (error) {
    console.error("Произошла ошибка:", error.message);
}

