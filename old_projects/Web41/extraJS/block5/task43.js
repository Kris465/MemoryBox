function totalSalaries(salaries) {

    const total = salaries.reduce((accumulator, currentValue) => accumulator + currentValue, 0);
    return total;
}


const salaries = [2500.50, 3000.00, 1800.75, 2200.25, 2700.00];

const result = totalSalaries(salaries);
console.log("Общая сумма выплаченных зарплат:", result.toFixed(2)); 