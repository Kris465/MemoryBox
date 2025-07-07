<?php

echo "Введите строку: ";
$text = trim(fgets(STDIN));

echo "Введите слово для поиска: ";
$search = trim(fgets(STDIN));

echo "Введите слово для замены: ";
$replace = trim(fgets(STDIN));

function replaceWord(string $string, string $search, string $replace): int {
    $count = 0;
    $string = str_replace($search, $replace, $string, $count);
    return $count;
}

$replacements = replaceWord($text, $search, $replace);

echo "\nРезультат:\n";
echo "Новая строка: " . $text . "\n";
echo "Количество замен: " . $replacements . "\n";
