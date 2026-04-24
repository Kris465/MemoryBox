<?php
$alpha_deg = isset($_GET['alpha']) ? floatval($_GET['alpha']) : null;
$v0 = isset($_GET['v0']) ? floatval($_GET['v0']) : null;
$R = isset($_GET['R']) ? floatval($_GET['R']) : null;
$H = isset($_GET['H']) ? floatval($_GET['H']) : null;

if (is_null($alpha_deg) || is_null($v0) || is_null($R) || is_null($H)) {
    echo "Пожалуйста, передайте параметры alpha, v0, R и H через URL.";
    exit;
}

$g = 9.8;
$alpha_rad = deg2rad($alpha_deg);
$t = $R / ($v0 * cos($alpha_rad));
$y = $v0 * $t * sin($alpha_rad) - ($g * $t * $t) / 2;

if ($y >= $H - 0.01 && $y <= $H + 0.01) {
    echo "Снаряд поразит цель.";
} else {
    echo "Снаряд не поразит цель.";
}
?>