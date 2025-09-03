<style>
ul.menu.main-menu, li.menu-item  {
    display: flex;
    align-items: center;
    list-style-type: none;
}
ul.menu.main-menu {
    width: 80%;
    padding: 0;
    margin: 0 auto;
    height: 50px;
    justify-content: space-between;
}
li.menu-item {
    background: #8bebf5;
    height: 100%;
    width: 100%;
    border: 1px solid #6f6f6f;
    justify-content: center;
}
li.menu-item a {
    color: #000;
    text-decoration: none;
}
.dropdown {
    background:rgb(245, 139, 240) !important;
}
.contact {
    background:rgb(245, 238, 139) !important;
}
</style>
<?php
/**
 * @param array        
 * @param string 
 * @return string 
 */
function buildMenu(array $items, string $menuClass = ''): string {
    if (empty($items)) {
        return '<div class="menu-empty">Меню пусто</div>';
    }
    $menuHtml = '<ul class="menu' . ($menuClass ? ' ' . htmlspecialchars($menuClass) : '') . '">';
    foreach ($items as $item) {
        if (!isset($item['text'])) {
            continue;
        }
        $text = htmlspecialchars($item['text'], ENT_QUOTES, 'UTF-8');
        $class = isset($item['class']) ? htmlspecialchars($item['class'], ENT_QUOTES, 'UTF-8') : '';
        $menuHtml .= '<li' . ($class ? ' class="' . $class . '"' : '') . '>';
        $menuHtml .= '<a href="#">' . $text . '</a>'; 
        $menuHtml .= '</li>';
    }
    $menuHtml .= '</ul>';
    return $menuHtml;
}
$menuItems = [
    ['text' => 'Главная', 'class' => 'menu-item active'],
    ['text' => 'О нас', 'class' => 'menu-item'],
    ['text' => 'Услуги', 'class' => 'menu-item dropdown'],
    ['text' => 'Контакты', 'class' => 'menu-item contact'],
];
echo buildMenu($menuItems, 'main-menu');
?>

