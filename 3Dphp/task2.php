<?php

function isPalindrome($string) {
    // Убираем пробелы и переводим строку в нижний регистр
    $cleanedString = preg_replace('/s+/', '', mb_strtolower($string));
    
    // Убираем все символы, кроме букв (русских и английских)
    $cleanedString = preg_replace('/[^p{L}]/u', '', $cleanedString);
    
    // Проверяем, является ли строка палиндромом
    return $cleanedString === strrev($cleanedString);
}

// Основной цикл для пользовательского ввода
while (true) {
    echo "Введите строку для проверки на палиндром (или 'exit' для выхода): ";
    $input = trim(fgets(STDIN)); // Читаем ввод пользователя

    if (strtolower($input) === 'exit') {
        break; // Выход из цикла, если пользователь ввел 'exit'
    }

    if (isPalindrome($input)) {
        echo "'$input' является палиндромом.\n";
    } else {
        echo "'$input' не является палиндромом.\n";
    }
}

echo "Выход из программы.\n";
?>
