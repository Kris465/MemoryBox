<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Фигуры на странице</title>
    <style>
        body {
            position: relative;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .square {
            width: 100px;
            height: 100px;
            background-color: red; 
            position: absolute;
            top: 50px; 
            left: 50px; 
        }
        .circle {
            width: 100px;
            height: 100px;
            background-color: blue; 
            border-radius: 50%;
            position: absolute;
            top: 200px; 
            left: 200px; 
        }
        .triangle {
            width: 0;
            height: 0;
            border-left: 50px solid transparent;
            border-right: 50px solid transparent;
            border-bottom: 100px solid green; 
            position: absolute;
            top: 400px; 
            left: 100px; 
        }
    </style>
</head>
<body>
    <div class="square"></div>
    <div class="circle"></div>
    <div class="triangle"></div>
</body>
</html>