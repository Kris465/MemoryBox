<?php
if (isset($_POST['a']) && isset($_POST['b'])) {
    $a = $_POST['a'];
    $b = $_POST['b'];

    $sum = $a + $b;      
    $diff = $a - $b;     
    $product = $a * $b;  
    $quotient = $a / $b; 

    echo "'$a' + '$b' = '$sum'<br>";       
    echo "'$a' - '$b' = '$diff'<br>";      
    echo "'$a' * '$b' = '$product'<br>";   
    echo "'$a' / '$b' = '$quotient'<br>"; 
} else {
    echo '<form method="post">
            Enter value for a: <input type="number" name="a"><br>
            Enter value for b: <input type="number" name="b"><br>
            <input type="submit" value="Calculate">
          </form>';
}
?>