<?php
session_start();
if (!isset($_SESSION['answers3'])) {
    header('Location: index.php');
    exit();
}


$correctAnswers1 = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'];
$correctAnswers2 = [
    ['a', 'b'], ['c'], ['a', 'd'], ['b'], ['c', 'd'], 
    ['a'], ['b', 'c'], ['d'], ['a', 'b'], ['c']
];
$correctAnswers3 = ['ответ1', 'ответ2', 'ответ3', 'ответ4', 'ответ5', 
                    'ответ6', 'ответ7', 'ответ8', 'ответ9', 'ответ10'];

$score1 = 0;
$score2 = 0;
$score3 = 0;


foreach ($_SESSION['answers1'] as $question => $answer) {
    $index = array_search($question, array_keys($correctAnswers1));
    if ($correctAnswers1[$index] == $answer) {
        $score1++;
    }
}
foreach ($_SESSION['answers2'] as $question => $answers) {
    $index = array_search($question, array_keys($correctAnswers2));
    if (is_array($answers) && !array_diff($correctAnswers2[$index], $answers) && !array_diff($answers, $correctAnswers2[$index])) {
        $score2 += 3; 
    }
}


foreach ($_SESSION['answers3'] as $question => $answer) {
    $index = array_search($question, array_keys($correctAnswers3));
    if (strtolower(trim($answer)) == strtolower(trim($correctAnswers3[$index]))) {
        $score3 += 5; 
    }
}

$totalScore = $score1 + $score2 + $score3;
?>

<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Результаты</title>
</head>
<body>
    <h1>Ваш результат</h1>
    <p>Баллы за первую страницу: <?php echo $score1; ?></p>
    <p>Баллы за вторую страницу: <?php echo $score2; ?></p>
    <p>Баллы за третью страницу: <?php echo $score3; ?></p>
    <p>Общий результат: <?php echo $totalScore; ?> баллов</p>
    <a href="index.php">Пройти тест снова</a>
</body>
</html>