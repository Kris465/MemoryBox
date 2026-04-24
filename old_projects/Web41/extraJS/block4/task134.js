function isLeapYear(year) {
    return (year % 400 === 0) || (year % 4 === 0 && year % 100 !== 0);
  }
  
  function getDaysInMonth(year) {
    return [
      31,
      isLeapYear(year) ? 29 : 28,
      31,
      30,
      31,
      30,
      31,
      31,
      30,
      31,
      30,
      31
    ];
  }
  
  function getPreviousAndNextDate(g, m, n) {
    
    if (m <1 || m >12) throw new Error("Неверный номер месяца");
    
    const daysInMonth = getDaysInMonth(g);
    
    if (n <1 || n > daysInMonth[m-1]) throw new Error("Неверное число месяца");
    
    let prevYear = g;
    let prevMonth = m;
    let prevDay = n -1;
    
    if (prevDay ===0) {
      prevMonth = m -1;
      
      if (prevMonth ===0) {
        prevMonth =12;
        prevYear = g -1;
      }
      
      const daysPrevMonth = getDaysInMonth(prevYear)[prevMonth-1];
      prevDay = daysPrevMonth;
      
    }
    
     let nextYear = g;
     let nextMonth = m;
     let nextDay = n +1;
  
     if (nextDay > daysInMonth[m-1]) {
       nextDay =1;
       nextMonth = m +1;
  
       if (nextMonth ===13) {
         nextMonth=1;
         nextYear= g +1;
       }
     }
  
     return {
       previous: { year: prevYear, month: prevMonth, day: prevDay },
       next: { year: nextYear, month: nextMonth, day: nextDay }
     };
  }
  
  const g =2024;
  const m =3;
  const n =1;
  
  const result = getPreviousAndNextDate(g,m,n);
  
  console.log(`${result.previous.day}.${result.previous.month}.${result.previous.year}`);
  console.log(`${result.next.day}.${result.next.month}.${result.next.year}`);