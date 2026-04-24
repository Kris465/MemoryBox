<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Перестановки трехзначного числа</title>
</head>
<body>
    <h1>Введите трехзначное число с различными цифрами</h1>
    <form method="post">
        <input type="number" name="number" min="100" max="999" required>
        <input type="submit" value="Отправить">
    </form>

    <?php
    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $inputNumber = $_POST['number'];

     
        if ($inputNumber >= 100 && $inputNumber <= 999) {
            $numberStr = (string)$inputNumber;
            $digits = str_split($numberStr);

            
            if (count(array_unique($digits)) === 3) {
               
                $permutations = getPermutations($digits);
                
                echo "<h2>Перестановки:</h2>";
                foreach ($permutations as $perm) {
                    echo implode('', $perm) . "<br>";
                }
            } else {
                echo "Ошибка: Все цифры должны быть различными.<br>";
            }
        } else {
            echo "Ошибка: Введите корректное трехзначное число.<br>";
        }
    }

    function getPermutations($items, $perms = []) {
        if (empty($items)) {
            return [$perms];
        }

        $result = [];
        for ($i = 0; $i < count($items); $i++) {
            $newItems = $items;
            $newPerms = array_merge($perms, [$newItems[$i]]);
            unset($newItems[$i]);
            $result = array_merge($result, getPermutations(array_values($newItems), $newPerms));
        }
        
        return $result;
    }
    ?>
</body>
</html>