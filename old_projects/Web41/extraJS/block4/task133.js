const prompt = require('prompt-sync')();

function getPreviousAndNextDay(m, n) {
    const daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];

    if (m < 1 || m > 12) {
      throw new Error("Неверный номер месяца");
    }
    
    if (n < 1 || n > daysInMonth[m - 1]) {
      throw new Error("Неверное число месяца");
    }
  
    let prevDay = n - 1;
    let prevMonth = m;
    
    if (prevDay === 0) {
      prevMonth = m - 1;
      prevDay = daysInMonth[prevMonth -1];
      if (prevMonth < 1) {
        throw new Error("Дата не может быть раньше чем 1 января");
      }
    }
  
    let nextDay = n + 1;
    let nextMonth = m;
  
    if (nextDay > daysInMonth[m -1]) {
      nextDay = 1;
      nextMonth = m +1;
      if (nextMonth >12) {
        throw new Error("Дата не может быть позже чем 31 декабря");
      }
    }
  
   return {
     previous: { month: prevMonth, day: prevDay },
     next: { month: nextMonth, day: nextDay }
   };
}

  const m =4; 
  const n =1; 
  
  const result = getPreviousAndNextDay(m,n);
  console.log(`Предыдущий день: ${result.previous.day}.${result.previous.month}`);
  console.log(`Следующий день: ${result.next.day}.${result.next.month}`);