<?php
function replaceWord($string, $searchWord, $replaceWord) {
    // Считаем количество вхождений
    $count = 0;

    // Используем preg_replace_callback для замены и подсчета замен
    $resultString = preg_replace_callback(
        '/' . preg_quote($searchWord, '/') . '/i', // Регистронезависимый поиск
        function ($matches) use (&$count, $replaceWord) {
            $count++; // Увеличиваем счетчик замен
            return $replaceWord; // Возвращаем слово для замены
        },
        $string
    );

    // Меняем оригинальную строку
    $string = $resultString;

    // Возвращаем количество замен
    return [$string, $count]; // Возвращаем измененную строку и количество замен
}

// Получаем ввод от пользователя
echo "Введите исходную строку: ";
$originalString = trim(fgets(STDIN)); // Читаем строку

echo "Введите слово для поиска: ";
$searchWord = trim(fgets(STDIN)); // Читаем слово для поиска

echo "Введите слово для замены: ";
$replaceWord = trim(fgets(STDIN)); // Читаем слово для замены

// Вызываем функцию с введенными параметрами
list($modifiedString, $numberOfReplacements) = replaceWord($originalString, $searchWord, $replaceWord);

// Выводим результаты
echo "Строка после изменения: " . $modifiedString . "\n"; // Выводим измененную строку
echo "Количество замен: " . $numberOfReplacements . "\n"; // Выводим количество замен
?>
