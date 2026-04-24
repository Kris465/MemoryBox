<?php
$a = 1; // начальная позиция белой фигуры (вертикаль)
$b = 2; // горизонталь
$c = 3; // позиция черной фигуры (вертикаль)
$d = 4; // горизонталь
$e = 5; // целевая позиция белой фигуры (вертикаль)
$f = 6; // горизонталь

function threat_rook($x1, $y1, $x2, $y2) {
    return ($x1 == $x2) || ($y1 == $y2);
}

function threat_bishop($x1, $y1, $x2, $y2) {
    return abs($x1 - $x2) == abs($y1 - $y2);
}

function threat_queen($x1, $y1, $x2, $y2) {
    return threat_rook($x1, $y1, $x2, $y2) || threat_bishop($x1, $y1, $x2, $y2);
}

function threat_knight($x1, $y1, $x2, $y2) {
    return (abs($x1 -$x2)==2 && abs($y1-$y2)==1) || (abs($x1-$x2)==1 && abs($y1-$y2)==2);
}

function threat_king($x1,$y1,$x2,$y2){
    return abs($x1-$x2)<=1 && abs($y1-$y2)<=1;
}

// Варианты проверки угрозы для каждой фигуры

// а) ладья и ладья
$cond_a = !threat_rook($c,$d,$e,$f);

// б) ладья и ферзь
$cond_b = !threat_queen($c,$d,$e,$f);

// в) ладья и конь
$cond_c = !threat_rook($c,$d,$e,$f) && !threat_knight($c,$d,$e,$f);

// г) ладья и слон
$cond_d = !threat_rook($c,$d,$e,$f) && !threat_bishop($c,$d,$e,$f);

// д) ферзь и ферзь
$cond_e = !threat_queen($c,$d,$e,$f);

// е) ферзь и ладья
$cond_f = !threat_queen($c,$d,$e,$f);

// ж) ферзь и конь
$cond_g = !threat_queen($c,$d,$e,$f) && !threat_knight($c,$d,$e,$f);

// з) ферзь и слон
$cond_h = !threat_queen($c,$d,$e,$f) && !threat_bishop($c,$d,$e,$f);

// и) конь и конь
$cond_i = !threat_knight($c,$d,$e,$f);

// к) конь и ладья
$cond_j= !threat_knight($c,$d,$e,$f)&&!threat_rook($c,$d,$e,$f);

// л) конь и ферзь
$cond_k= !threat_knight($c,$d,$e,$f)&&!threat_queen($c,$d,$e,$f);

// м) конь и слон
$cond_l= !threat_knight($c,$d,$e,$f)&&!threat_bishop($c,$d,$e,$f);

// н) слон и слон
$cond_m= !threat_bishop($c,$d,$e,$f);

// о) слон и ферзь
$cond_n= !threat_bishop($c,$d,$e,$f)&&!threat_queen($c,$d,$e,$f);

// п) слон и конь
$cond_o= !threat_bishop($c,$d,$e,$f)&&!threat_knight($c,$d,$e,$f);

// р) слон и ладья
$cond_p= !threat_bishop($c,$d,$e,$f)&&!threat_rook($c,$d,$e,$f);

// с) король и слон
$cond_q= !(abs($c-$e)<=1 && abs($d-$f)<=1 && threat_bishop($c,$d,$e,$f));

// т) король и ферзь
$cond_r= !(abs($c-$e)<=1 && abs($d-$f)<=1 && threat_queen($c,$d,$e,$f));

// у) король и конь
$cond_s= !(abs($c-$e)<=1 && abs($d-$f)<=1 && threat_knight($c,$d,$e,$f));

// ф ) король и ладья
$cond_t= !(abs($c-$e)<=1 && abs($d-$f)<=1 && threat_rook($c,$d,$e,$f));

echo "а): " . ($cond_a ? "может" : "не может") . "<br>";
echo "б): " . ($cond_b ? "может" : "не может") . "<br>";
echo "в): " . ($cond_c ? "может" : "не может") . "<br>";
echo "г): " . ($cond_d ? "может" : "не может") . "<br>";
echo "д): " . ($cond_e ? "может" : "не может") . "<br>";
echo "е): " . ($cond_f ? "может" : "не может") . "<br>";
echo "ж): " . ($cond_g ? "может" : "не может") . "<br>";
echo "з): " . ($cond_h ? "может" : "не может") . "<br>";
echo "и): " . ($cond_i ? "может" : "не может") . "<br>";
echo("к): ". ($cond_j ? "может" : "не может")."<br>");
echo("л): ". ($cond_k ? "может" : "не может")."<br>");
echo("м): ". ($cond_l ? "может" : "не может")."<br>");
echo("н): ". ($cond_m ? "может" : "не может")."<br>");
echo("о): ". ($cond_n ? "может" : "не может")."<br>");
echo("п): ". ($cond_o ? "может" : "не может")."<br>");
echo("р): ". ($cond_p ? "может" : "не может")."<br>");
echo("с): ". ($cond_q ? "может" : "не может")."<br>");
echo("т): ". ($cond_r ? "может" : "не может")."<br>");
echo("у): ". ($cond_s ? "может" : "не может")."<br>");
echo("ф): ". ($cond_t ? "может" : "не может")."<br>");
?>

