<?php
function isPalindrome($string) {
    // Убираем пробелы и приводим строку к нижнему регистру
    $cleanedString = preg_replace('/s+/', '', mb_strtolower($string, 'UTF-8'));
    
    // Убираем все символы, кроме букв (русские и английские)
    $cleanedString = preg_replace('/[^а-яёa-z]/iu', '', $cleanedString);

    // Проверяем, равна ли строка своей обратной версии
    return $cleanedString === mb_strrev($cleanedString);
}

// Функция для реверсирования строки с поддержкой многобайтовых символов
function mb_strrev($string) {
    return mb_convert_encoding(strrev(mb_convert_encoding($string, 'UTF-16LE', 'UTF-8')), 'UTF-8', 'UTF-16LE');
}

// Получаем ввод от пользователя
echo "Введите строку для проверки: ";
$inputString = trim(fgets(STDIN)); // Читаем строку

// Проверяем, является ли строка палиндромом
if (isPalindrome($inputString)) {
    echo "Строка является палиндромом.\n";
} else {
    echo "Строка не является палиндромом.\n";
}
?>
