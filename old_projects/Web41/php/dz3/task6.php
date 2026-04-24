<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Календарь на текущий месяц</title>
    <style>
        .calendar {
            display: grid;
            grid-template-columns: repeat(7, 1fr);
            gap: 10px;
            margin: 20px;
        }

        .day {
            padding: 15px;
            text-align: center;
            border: 1px solid #ccc;
            border-radius: 5px;
            transition: background-color 0.3s, color 0.3s;
        }

        .weekend {
            color: red;
        }

        .holiday {
            color: red;
        }

        .today {
            border: 3px solid blue;
        }

        .day:hover {
            background-color: red;
            color: white;
        }
    </style>
</head>
<body>

<?php
$currentDate = new DateTime();
$currentMonth = $currentDate->format('m');
$currentYear = $currentDate->format('Y');
$currentDay = $currentDate->format('d');

$holidays = [
    '01-01',  
    '07-01',  
    '08-03', 
    '01-05',  
    '09-05',  
];

$firstDayOfMonth = new DateTime("first day of $currentYear-$currentMonth");
$lastDayOfMonth = new DateTime("last day of $currentYear-$currentMonth");

echo '<div class="calendar">';
for ($i = $firstDayOfMonth->format('w'); $i > 0; $i--) {
    echo '<div class="day"></div>';  
}

for ($day = 1; $day <= $lastDayOfMonth->format('d'); $day++) {
    $dateString = sprintf('%02d-%02d', $day, $currentMonth);
    $class = "day";

    $dayOfWeek = (new DateTime("$currentYear-$currentMonth-$day"))->format('w');
    if ($dayOfWeek == 0 || $dayOfWeek == 6) { 
        $class .= ' weekend';
    }

    if (in_array($dateString, $holidays)) {
        $class .= ' holiday';
    }

    if ($day == $currentDay) {
        $class .= ' today';
    }

    echo "<div class=\"$class\">$day</div>";
}
echo '</div>';
?>

</body>
</html>