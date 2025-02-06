<?php
function isPalindrome($string) {
    $string = mb_strtolower(trim($string));
    $string = preg_replace('/[^p{L}]/u', '', $string);
    return $string === strrev($string);
}

echo "Введите строку: ";
$handle = fopen("php://stdin", "r");
$userInput = fgets($handle);

if (isPalindrome($userInput)) {
    echo "Строка является палиндромом.\n";
} else {
    echo "Строка не является палиндромом.\n";
}
?>
