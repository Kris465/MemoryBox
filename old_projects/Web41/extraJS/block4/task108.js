const prompt = require('prompt-sync')();

function getSuitName(m) {
    switch (m) {
        case 1:
            return "Пики";
        case 2:
            return "Трефы";
        case 3:
            return "Бубны";
        case 4:
            return "Червы";
        default:
            return "Некорректный номер масти. Пожалуйста, введите число от 1 до 4.";
    }
}


const suitNumber = parseInt(prompt("Введите номер масти (1 - Пики, 2 - Трефы, 3 - Бубны, 4 - Червы):"), 10);


if (!isNaN(suitNumber)) {
    const suitName = getSuitName(suitNumber);

    console.log(`Название масти: ${suitName}`);
} else {
    console.log("Пожалуйста, введите корректное число.");
}