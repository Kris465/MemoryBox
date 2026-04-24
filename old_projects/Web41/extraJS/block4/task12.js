const prompt = require('prompt-sync')();
function calculateCurrent(voltage, resistance) {
    return voltage / resistance; 
}


function compareCurrents(voltage1, resistance1, voltage2, resistance2) {
    const current1 = calculateCurrent(voltage1, resistance1); 
    const current2 = calculateCurrent(voltage2, resistance2); 

    console.log(`Ток первого участка: ${current1.toFixed(4)} А`);
    console.log(`Ток второго участка: ${current2.toFixed(4)} А`);

    if (current1 < current2) {
        console.log("По первому участку протекает меньший ток.");
    } else if (current1 > current2) {
        console.log("По второму участку протекает меньший ток.");
    } else {
        console.log("Токи по обоим участкам равны.");
    }
}


const voltage1 = parseFloat(prompt("Введите напряжение на первом участке (в В):"));
const resistance1 = parseFloat(prompt("Введите сопротивление первого участка (в Ом):"));
const voltage2 = parseFloat(prompt("Введите напряжение на втором участке (в В):"));
const resistance2 = parseFloat(prompt("Введите сопротивление второго участка (в Ом):"));


compareCurrents(voltage1, resistance1, voltage2, resistance2);