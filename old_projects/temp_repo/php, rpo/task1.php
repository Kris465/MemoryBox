<?php

function replaceWord(&$string, $search, $replace) {
    // Используем функцию str_replace для замены слов
    $originalString = $string; // Сохраняем оригинальную строку для подсчета замен
    $string = str_replace($search, $replace, $string); // Заменяем слова

    // Подсчитываем количество замен
    $count = substr_count($originalString, $search);
    
    return $count; // Возвращаем количество замен
}

// Пример использования
$originalString = "cat runs to another cat";
$searchWord = "cat";
$replaceWord = "bull";

$countReplacements = replaceWord($originalString, $searchWord, $replaceWord);

echo "Измененная строка: $originalString\n"; // bull runs to another bull
echo "Количество замен: $countReplacements\n"; // 2

?>
