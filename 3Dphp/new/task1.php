<?php

echo "Введите строку: ";
$text = trim(fgets(STDIN));

echo "Введите слово для поиска: ";
$search = trim(fgets(STDIN));

echo "Введите слово для замены: ";
$replace = trim(fgets(STDIN));

function replaceWord(string $string, string $search, string $replace): array {
    $count = 0;
    $newString = str_replace($search, $replace, $string, $count);
    return ['count' => $count, 'newString' => $newString];
}

$result = replaceWord($text, $search, $replace);

echo "\nРезультат:\n";
echo "Новая строка: " . $result['newString'] . "\n";
echo "Количество замен: " . $result['count'] . "\n";