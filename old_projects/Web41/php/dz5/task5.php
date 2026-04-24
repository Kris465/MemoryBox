<?php
$processors = [
    [
        'название' => 'Intel Core i7-11700K',
        'сокет' => 'LGA 1200',
        'частота' => '3.6 GHz',
        'количество_ядер' => 8
    ],
    [
        'название' => 'AMD Ryzen 7 5800X',
        'сокет' => 'AM4',
        'частота' => '3.8 GHz',
        'количество_ядер' => 8
    ]
];

$motherboards = [
    [
        'название' => 'ASUS ROG Strix Z590-E',
        'сокет' => 'LGA 1200',
        'тип_памяти' => 'DDR4'
    ],
    [
        'название' => 'MSI B550-A PRO',
        'сокет' => 'AM4',
        'тип_памяти' => 'DDR4'
    ]
];

$rams = [
    [
        'название' => 'Corsair Vengeance LPX',
        'тип_памяти' => 'DDR4',
        'объем' => '16 GB'
    ],
    [
        'название' => 'G.Skill Ripjaws V',
        'тип_памяти' => 'DDR4',
        'объем' => '32 GB'
    ]
];

$hdds = [
    [
        'название' => 'Seagate Barracuda',
        'тип_диска' => 'HDD',
        'объем' => '2 TB'
    ],
    [
        'название' => 'Samsung 970 EVO',
        'тип_диска' => 'SSD',
        'объем' => '1 TB'
    ]
];

$powerSupplies = [
    [
        'название' => 'Corsair RM750x',
        'мощность' => '750W'
    ],
    [
        'название' => 'EVGA 600 W1',
        'мощность' => '600W'
    ]
];

$combinations = [];

foreach ($processors as $processor) {
    foreach ($motherboards as $motherboard) {
        foreach ($rams as $ram) {
            foreach ($hdds as $hdd) {
                foreach ($powerSupplies as $powerSupply) {
                    if ($processor['сокет'] === $motherboard['сокет'] && $ram['тип_памяти'] === $motherboard['тип_памяти']) {
                        $combinations[] = [
                            'Процессор' => $processor,
                            'Материнская плата' => $motherboard,
                            'Оперативная память' => $ram,
                            'Жесткий диск' => $hdd,
                            'Блок питания' => $powerSupply
                        ];
                    }
                }
            }
        }
    }
}

echo "<h1>Возможные комбинации ПК</h1>";
foreach ($combinations as $index => $combination) {
    echo "<h2>Комбинация " . ($index + 1) . "</h2>";
    echo "<strong>Процессор:</strong> " . $combination['Процессор']['название'] . "<br>";
    echo "Сокет: " . $combination['Процессор']['сокет'] . "<br>";
    echo "Частота: " . $combination['Процессор']['частота'] . "<br>";
    echo "Количество ядер: " . $combination['Процессор']['количество_ядер'] . "<br><br>";

    echo "<strong>Материнская плата:</strong> " . $combination['Материнская плата']['название'] . "<br>";
    echo "Сокет: " . $combination['Материнская плата']['сокет'] . "<br>";
    echo "Тип памяти: " . $combination['Материнская плата']['тип_памяти'] . "<br><br>";

    echo "<strong>Оперативная память:</strong> " . $combination['Оперативная память']['название'] . "<br>";
    echo "Тип памяти: " . $combination['Оперативная память']['тип_памяти'] . "<br>";
    echo "Объем: " . $combination['Оперативная память']['объем'] . "<br><br>";

    echo "<strong>Жесткий диск:</strong> " . $combination['Жесткий диск']['название'] . "<br>";
    echo "Тип диска: " . $combination['Жесткий диск']['тип_диска'] . "<br>";
    echo "Объем: " . $combination['Жесткий диск']['объем'] . "<br><br>";

    echo "<strong>Блок питания:</strong> " . $combination['Блок питания']['название'] . "<br>";
    echo "Мощность: " . $combination['Блок питания']['мощность'] . "<br><br>";
}
?>