<?php

function calculateValues() {
    $x = 10; 
    $x = 10; 
    echo "Значение x после пункта а: $x\n";

    $x = 17.5; 
    $x = 2; 
    $x = $x; 
    echo "Значение x после пункта б: $x\n"; // x = 2

    $x = 60; 
    $x = 1;
    $x = 0;
    echo "Значение x после пункта в: $x\n";

    $x = 50; 
    $x = 25; 
    $k = $x; 
    echo "Значение x после пункта г: $x, значение k: $k\n"; 
}

calculateValues();
?>