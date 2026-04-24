<?php
session_start(); 


$score1 = isset($_SESSION['score1']) ? $_SESSION['score1'] : 0;
$score2 = isset($_SESSION['score2']) ? $_SESSION['score2'] : 0;
$score3 = isset($_SESSION['score3']) ? $_SESSION['score3'] : 0;




$totalScore = $score1 + $score2 + $score3;

echo $totalScore;


