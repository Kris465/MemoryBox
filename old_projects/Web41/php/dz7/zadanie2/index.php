<?php
session_start(); // Инициализация сессии

// Сбрасываем предыдущие результаты, если они есть
unset($_SESSION['score1']);
unset($_SESSION['score2']);
unset($_SESSION['score3']);

// Перенаправляем на первую страницу теста
header('Location: questions1.php');
exit();
?>