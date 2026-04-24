
const prompt = require('prompt-sync')(); 
const monitorPrice = Number(prompt("введите цену монитора: "));
const blockPrice = Number(prompt("введите цену системного блока: "));
const keyboardPrice = Number(prompt("введите цену клавиатуры: "));
const mousePrice = Number(prompt("введите цену мышки: "));
const n = Number(prompt("Введите колличество компьютеров: "));
  

function calculateCost(monitor, block, keyboard, mouse, n) {
    const computerCost = monitor + block + keyboard + mouse;
    return computerCost * n;
  }

  const numComputers = 3; 
  const totalCost = calculateCost(monitorPrice, blockPrice, keyboardPrice, mousePrice, numComputers);
  const totalCost1 = calculateCost(monitorPrice, blockPrice, keyboardPrice, mousePrice, n);
  
  console.log(`компьютеров: ${n} стоят: ${totalCost1}`);
  console.log(`Стоимость 3 компьютеров: ${totalCost}`);