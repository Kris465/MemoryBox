<?php
function replaceWord($string, $searchWord, $replaceWord) {
    $count = 0;
    $resultString = preg_replace_callback(
        '/' . preg_quote($searchWord, '/') . '/i',
        function ($matches) use (&$count, $replaceWord) {
            $count++;
            return $replaceWord;
        },
        $string
    );
    $string = $resultString;
    return [$string, $count];
}

echo "Введите исходную строку: ";
$originalString = trim(fgets(STDIN));

echo "Введите слово для поиска: ";
$searchWord = trim(fgets(STDIN));

echo "Введите слово для замены: ";
$replaceWord = trim(fgets(STDIN));

list($modifiedString, $numberOfReplacements) = replaceWord($originalString, $searchWord, $replaceWord);

echo "Строка после изменения: " . $modifiedString . "\n";
echo "Количество замен: " . $numberOfReplacements . "\n";
?>
