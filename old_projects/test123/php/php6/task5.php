<?php
$processors = [
    [
        'название' => 'Intel Core i7-9700K',
        'сокет' => 'LGA1151',
        'частота' => '3.6 GHz',
        'количество ядер' => 8
    ],
    [
        'название' => 'AMD Ryzen 7 3700X',
        'сокет' => 'AM4',
        'частота' => '3.6 GHz',
        'количество ядер' => 8
    ]
];

$motherboards = [
    [
        'название' => 'ASUS ROG Strix Z390-E',
        'сокет' => 'LGA1151',
        'тип памяти' => 'DDR4'
    ],
    [
        'название' => 'MSI B450 TOMAHAWK MAX',
        'сокет' => 'AM4',
        'тип памяти' => 'DDR4'
    ]
];

$rams = [
    [
        'название' => 'Corsair Vengeance LPX 16GB',
        'тип памяти' => 'DDR4',
        'объем памяти' => '16GB'
    ],
    [
        'название' => 'G.Skill Trident Z RGB 32GB',
        'тип памяти' => 'DDR4',
        'объем памяти' => '32GB'
    ]
];

$hardDrives = [
    [
        'название' => 'Samsung 970 EVO 1TB',
        'тип диска' => 'SSD',
        'объем' => '1TB'
    ],
    [
        'название' => 'Seagate BarraCuda 2TB',
        'тип диска' => 'HDD',
        'объем' => '2TB'
    ]
];

$powerSupplies = [
    [
        'название' => 'Corsair RM750x',
        'мощность' => '750W'
    ],
    [
        'название' => 'EVGA SuperNOVA 650 G5',
        'мощность' => '650W'
    ]
];

function generatePCCombinations($processors, $motherboards, $rams, $hardDrives, $powerSupplies) {
    $combinations = [];

    foreach ($processors as $processor) {
        foreach ($motherboards as $motherboard) {
            if ($processor['сокет'] == $motherboard['сокет']) {
                foreach ($rams as $ram) {
                    if ($ram['тип памяти'] == $motherboard['тип памяти']) {
                        foreach ($hardDrives as $hardDrive) {
                            foreach ($powerSupplies as $powerSupply) {
                                $combinations[] = [
                                    'Процессор' => $processor['название'],
                                    'Материнская плата' => $motherboard['название'],
                                    'Оперативная память' => $ram['название'],
                                    'Жесткий диск' => $hardDrive['название'],
                                    'Блок питания' => $powerSupply['название']
                                ];
                            }
                        }
                    }
                }
            }
        }
    }

    return $combinations;
}

$pcCombinations = generatePCCombinations($processors, $motherboards, $rams, $hardDrives, $powerSupplies);

?>
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Комбинации ПК</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            padding: 20px;
        }
        .pc-combination {
            background-color: #ffffff;
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .pc-combination h3 {
            margin-top: 0;
            color: #333;
        }
        .pc-combination p {
            margin: 5px 0;
            color: #555;
        }
        .pc-combination:nth-child(odd) {
            background-color: #e3f2fd;
        }
        .pc-combination:nth-child(even) {
            background-color: #fff3e0;
        }
    </style>
</head>
<body>
    <h1>Возможные комбинации ПК</h1>
    <?php foreach ($pcCombinations as $combination): ?>
        <div class="pc-combination">
            <h3>Комбинация ПК</h3>
            <p><strong>Процессор:</strong> <?php echo $combination['Процессор']; ?></p>
            <p><strong>Материнская плата:</strong> <?php echo $combination['Материнская плата']; ?></p>
            <p><strong>Оперативная память:</strong> <?php echo $combination['Оперативная память']; ?></p>
            <p><strong>Жесткий диск:</strong> <?php echo $combination['Жесткий диск']; ?></p>
            <p><strong>Блок питания:</strong> <?php echo $combination['Блок питания']; ?></p>
        </div>
    <?php endforeach; ?>
</body>
</html>