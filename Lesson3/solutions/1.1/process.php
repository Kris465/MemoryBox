<?php
$name = '';
$message = '';

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars($_POST['name']);
    $message = "Приятно познакомиться, $name!";
}
?>
