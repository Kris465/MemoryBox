const prompt = require('prompt-sync')();


const swapCaseAndReplaceDigits = (str) => 
    str.replace(/\w/g, (char) => 
      /\d/.test(char) ? '_' : char === char.toUpperCase() ? char.toLowerCase() : char.toUpperCase()
    );
  

  const userInput = prompt("Введите строку:");
  

  if (userInput !== null) {
    const result = swapCaseAndReplaceDigits(userInput);
    console.log("Результат:", result);
  } else {
    console.log("Ввод отменен.");
  }

