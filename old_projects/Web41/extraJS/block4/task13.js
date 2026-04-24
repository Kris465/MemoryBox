function hasRealRoots(a, b, c) {
    const D = b * b - 4 * a * c;
    if (D > 0) {
        console.log("Уравнение имеет два различных вещественных корня.");
    } else if (D === 0) {
        console.log("Уравнение имеет один вещественный корень (двойной корень).");
    } else {
        console.log("Уравнение не имеет вещественных корней.");
    }
}
const a = parseFloat(prompt("Введите значение a (a > 0):"));
if (a <= 0) {
    console.log("Значение a должно быть больше 0.");
} else {
    const b = parseFloat(prompt("Введите значение b:"));
    const c = parseFloat(prompt("Введите значение c:"));
    hasRealRoots(a, b, c);
}