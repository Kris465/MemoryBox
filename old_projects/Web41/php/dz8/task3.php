<?php
function buildMenu($menuItems) {

    $html = '<ul style="list-style-type: none; padding: 0; display: flex;">';

    foreach ($menuItems as $item) {

        if (isset($item['text']) && isset($item['class']) && isset($item['bgColor']) && isset($item['textColor'])) {

            $html .= '<li class="' . htmlspecialchars($item['class']) . '" style="background-color: ' . htmlspecialchars($item['bgColor']) . '; color: ' . htmlspecialchars($item['textColor']) . '; padding: 10px 20px; margin: 5px; display: inline-block;">' . htmlspecialchars($item['text']) . '</li>';
        }
    }

    $html .= '</ul>';

    return $html;
}

$menuItems = [
    ['text' => 'Главная', 'class' => 'menu-item', 'bgColor' => '#4CAF50', 'textColor' => '#FFFFFF'],
    ['text' => 'О нас', 'class' => 'menu-item', 'bgColor' => '#2196F3', 'textColor' => '#FFFFFF'],
    ['text' => 'Услуги', 'class' => 'menu-item', 'bgColor' => '#FF9800', 'textColor' => '#FFFFFF'],
    ['text' => 'Контакты', 'class' => 'menu-item', 'bgColor' => '#F44336', 'textColor' => '#FFFFFF'],
];

$menuHtml = buildMenu($menuItems);

echo $menuHtml;
?>