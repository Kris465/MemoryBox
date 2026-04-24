function calculateDepositGrowth(initialAmount, monthlyRate, months) {
    const growth = [];
    const totalAmounts = [];

    let currentAmount = initialAmount;

    for (let month = 1; month <= months; month++) {
        const increase = currentAmount * (monthlyRate / 100);
        growth.push(increase);
        currentAmount += increase;
        totalAmounts.push(currentAmount);
    }

    return { growth, totalAmounts };
}

const initialAmount = 1000;
const monthlyRate = 2; // 2%
const totalMonths = 12;

const { growth, totalAmounts } = calculateDepositGrowth(initialAmount, monthlyRate, totalMonths);

console.log("Прирост суммы вклада за первый, второй, ..., десятый месяц:");
for (let i = 0; i < 10; i++) {
    console.log(`Месяц ${i + 1}: ${growth[i].toFixed(2)} руб.`);
}

console.log("\nСумма вклада через три, четыре, ..., двенадцать месяцев:");
for (let i = 2; i < totalMonths; i++) {
    console.log(`Через ${i + 1} месяц(а): ${totalAmounts[i].toFixed(2)} руб.`);
}