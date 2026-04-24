function calculateAge(birthYear, birthMonth, currentYear, currentMonth) {
    let years = currentYear - birthYear;
    let months = currentMonth - birthMonth;

    if (months < 0) {
      years -= 1;
      months += 12;
    }

    return { years: years, months: months };
  }

  const birthYear = 1990;
  const birthMonth = 2; 
  const currentYear = 2024;
  const currentMonth = 5; 
  
  const age = calculateAge(birthYear, birthMonth, currentYear, currentMonth);
  console.log(`Возраст: ${age.years} лет и ${age.months} месяцев`);