<?php
function checkDivision($a, $b) {
    return (int)(($a % $b == 0) || ($b % $a == 0));
}


echo checkDivision(10, 5); 
echo checkDivision(7, 14); 
echo checkDivision(3, 5);  
echo checkDivision(0, 5);  
echo checkDivision(5, 0);  
?>