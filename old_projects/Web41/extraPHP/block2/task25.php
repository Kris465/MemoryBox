<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Нахождение числа x по n</title>
</head>
<body>
    <h1>Введите число n (10 ≤ n ≤ 999 и десятков не равно нулю)</h1>
    <form method="post">
        <input type="number" name="n" min="10" max="999" required>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $n = intval($_POST['n']);


        if ($n >= 10 && $n <= 999 && (($n / 10) % 10) != 0) {
  
            function findX($n) {
          
                $c = $n % 10;
                
                
                $nWithoutLastDigit = ($n - $c) / 10; 
                

                $b = $nWithoutLastDigit % 10;
                $a = ($nWithoutLastDigit - $b) / 10; 
            
                
                return (100 * $a) + (10 * $b) + $c;
            }

            $x = findX($n);
            
            echo "<h2>Найдено число x: " . htmlspecialchars($x) . "</h2>";
        } else {
            echo "<h2 style='color: red;'>Ошибка: Убедитесь, что число находится в диапазоне от 10 до 999 и десятков не равно нулю</h2>";
        }
    }
    ?>
</body>
</html>