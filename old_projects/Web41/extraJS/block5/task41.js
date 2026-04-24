function totalMass(masses) {
    const total = masses.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    return total;
}

const masses = [2.5, 3.0, 1.2, 4.8, 2.1, 3.3, 5.0, 1.5, 2.7, 4.0, 3.6, 2.9]; 

const result = totalMass(masses);
console.log("Общая масса всех предметов:", result);