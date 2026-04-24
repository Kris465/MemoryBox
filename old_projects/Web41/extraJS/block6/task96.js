const prompt = require('prompt-sync')(); 

// Функция для проверки корректности ввода роста учеников
function getValidatedHeights() {
  while (true) {
    const input = prompt("Введите рост 15 юношей через пробел (по убыванию, без повторений):");
    if (!input) continue;
    
    const numbers = input.trim().split(/\s+/).map(Number);
    
    // Проверяем что ровно 15 чисел и они упорядочены по убыванию
    if (numbers.length === 15 && !numbers.some(isNaN)) {
      let valid = true;
      for (let i = 0; i < numbers.length - 1; i++) {
        if (numbers[i] <= numbers[i + 1]) {
          valid = false;
          break;
        }
      }
      if (valid) return numbers;
    }
    alert("Ошибка ввода! Введите ровно 15 чисел через пробел, упорядоченных строго по убыванию без повторений.");
  }
}

// Функция для проверки роста нового ученика
function getValidatedNewHeight(min, max) {
  while (true) {
    const input = Number(prompt(`Введите рост нового ученика (должен быть между ${min} и ${max}, не совпадать ни с одним существующим):`));
    if (!isNaN(input) && input > min && input < max && !heights.includes(input)) {
      return input;
    }
    alert(`Ошибка! Рост должен быть числом между ${min} и ${max} и не совпадать с существующими.`);
  }
}

// Основная программа
try {
  console.log("Программа для определения места нового ученика в списке ростов");
  
  // Получаем и проверяем данные
  const heights = getValidatedHeights();
  const minHeight = heights[heights.length - 1];
  const maxHeight = heights[0];
  
  console.log("Введенные роста учеников:", heights.join(', '));
  console.log(`Минимальный рост: ${minHeight}, Максимальный рост: ${maxHeight}`);
  
  const newHeight = getValidatedNewHeight(minHeight, maxHeight);
  console.log(`Рост нового ученика: ${newHeight}`);
  
  // Находим позицию без использования условных операторов
  const position = heights.findIndex(h => h < newHeight) + 1;
  
  // Выводим результат в консоль
  console.log(`Рост нового ученика займет ${position}-е место в списке`);
  
} catch (e) {
  console.error("Произошла ошибка:", e.message);
}