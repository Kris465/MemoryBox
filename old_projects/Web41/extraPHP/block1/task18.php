<?php

function calculateValues() {
    $s = 5; 
    $s = 57;
    echo "Значение s после пункта а: $s\n"; 

    $s = 6;
    $s = 5.2;
    $s = 0; 
    echo "Значение s после пункта б: $s\n"; 

    $s = 7.5; 
    $s = 2;
    $s = $s; 
    echo "Значение s после пункта в: $s\n"; 

    $s = 45; 
    $s = 25; 
    $k = $s;
    echo "Значение s после пункта г: $s, значение k: $k\n"; 
}

calculateValues();
?>