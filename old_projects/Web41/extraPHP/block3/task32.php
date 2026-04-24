<?php
function isPointInShadedArea($x, $y) {
    $inCircle = ($x * $x + $y * $y <= 4); 
    
    $inRectangle = ($x >= -1 && $x <= 1 && $y >= -1 && $y <= 1);
    
    $inTriangle = ($y >= 0 && $y <= -abs($x) + 2);
    
    return $inCircle || $inRectangle || $inTriangle;
}

$points = [
    [0, 0],    
    [1, 1],    
    [2, 0],    
    [3, 3],    
    [-1, -1],  
    [0, 2],    
    [1.5, 0.5] 
];

foreach ($points as $point) {
    $x = $point[0];
    $y = $point[1];
    $result = isPointInShadedArea($x, $y);
    echo "Точка ($x, $y): " . ($result ? "Входит" : "Не входит") . "\n";
}
?>