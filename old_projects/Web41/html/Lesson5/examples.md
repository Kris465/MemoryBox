# Примеры:

1. Плавное изменение цвета фона

```html
<div class="color-change"></div>
```

```css
.color-change {
    width: 200px;
    height: 200px;
    background-color: #3498db;
    transition: background-color 0.5s ease;
}

.color-change:hover {
    background-color: #e74c3c;
}
```

2. Увеличение размера при наведении

```html
<div class="scale-up"></div>
```

```css
.scale-up {
    width: 100px;
    height: 100px;
    background-color: #2ecc71;
    transition: transform 0.3s ease;
}

.scale-up:hover {
    transform: scale(1.5);
}
```

3. Вращение элемента

```html
<div class="rotate"></div>
```

```css
.rotate {
    width: 100px;
    height: 100px;
    background-color: #f39c12;
    animation: spin 2s linear infinite;
}

@keyframes spin {
    from { transform: rotate(0deg); }
    to { transform: rotate(360deg); }
}
```

4. Плавное появление текста
```html
<div class="fade-in">Hello, World!</div>
```

```css
.fade-in {
    opacity: 0;
    animation: fadeIn 2s forwards;
}

@keyframes fadeIn {
    to { opacity: 1; }
}
```

5. Бегущая строка
```html
<div class="marquee">This is a running text example.</div>
```

```css
.marquee {
    width: 100%;
    overflow: hidden;
    white-space: nowrap;
    box-sizing: border-box;
}

.marquee::after {
    content: attr(data-text);
    display: inline-block;
    animation: marquee 10s linear infinite;
}

@keyframes marquee {
    from { transform: translateX(100%); }
    to { transform: translateX(-100%); }
}
```

6. Пульсация элемента

```html
<div class="pulse"></div>
```

```css
.pulse {
    width: 100px;
    height: 100px;
    background-color: #9b59b6;
    border-radius: 50%;
    animation: pulse 1.5s infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.2); }
}
```

7. Сдвиг элемента

```html
<div class="slide"></div>
```

```css
.slide {
    width: 100px;
    height: 100px;
    background-color: #e67e22;
    position: relative;
    animation: slideIn 1s forwards;
}

@keyframes slideIn {
    from { left: -150px; }
    to { left: 0; }
}
```

8. Вспышка кнопки
```html
<button class="flash-button">Click Me!</button>
```

```css
.flash-button {
    padding: 10px 20px;
    background-color: #2980b9;
    color: white;
    border: none;
    cursor: pointer;
    animation: flash 1s infinite alternate;
}

@keyframes flash {
    from { opacity: 1; }
    to { opacity: 0.5; }
}
```

9. Перемещение по кругу
```html
<div class="circle"></div>
```
```css
.circle {
    width: 50px;
    height: 50px;
    background-color: #34495e;
    border-radius: 50%;
    position: relative;
    animation: circleMove 4s linear infinite;
}

@keyframes circleMove {
    from { transform: translate(0, 0); }
    to { transform: translate(100px, 100px); }
}
```

10. Смена шрифта и размера текста

```html
<h1 class="text-change">Welcome!</h1>
```

```css
.text-change {
    font-size: 30px;
    transition: font-size 0.5s ease, color 0.5s ease;
}

.text-change:hover {
    font-size: 50px;
    color: #e74c3c;
}
```
