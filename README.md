# Викторина

Задача 1: В программе adobe illustrator создайте фон с абстрактным градиентным изображением (используйте разные виды кистей и кривизну). Следуйте указаниям учителя, но попробуйте создать что-то свое и уникальное. Создайте папку images. Экспортируйте фон под названием Background.png в папку images.

Задача 2: Придумайте 5 вопросов для викторины, найдите или создайте в adobe illustrator пять изображений. По одному для каждого вопроса и тоже поместите их в папку images, а также назовите их image1.jpg – image2.jpg и т.д.

Задача 3:  Создайте новую папку. Поместите в нее папку images. Поместите в папку с проектом шаблон кода (из сетевой папки) и откройте ее через vs code. Шаблон выглядит так:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Заголовок страницы</title>
</head>
<body>
    <header>
        <h1>Заголовок страницы</h1>
    </header>

    <div> …
    </div>
</body>
</html> 
```

Задача 4: Итак, создаем файл styles.css и script.js. Cтруктура нашего проекта будет выглядеть знакомо нам, но помимо привычных: index.html, styles.css и script.js, добавилась папка с картинками – images. Открываем index.html и видоизменяем его под наш проект:

```html
<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Викторина</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
</head>

<body>
    <div class="background"></div>
    <div class="quiz-container">
        <h1>Добро пожаловать, смельчак! Давай посмотрим, на что ты способен!</h1>
        <img id="question-image" src="" alt="Изображение к вопросу" style="display: none;">
        
        <p id="question">Ваш вопрос появится здесь</p>

        <div class="options">
            <button id="option1">Вариант 1</button>
            <button id="option2">Вариант 2</button>
            <button id="option3">Вариант 3</button>
        </div>

        <button id="next-button">Далее</button>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

Задача 5: Открываем styles.css и помещаем в него стили:

```css
body {
    font-family: 'Arial', sans-serif;
    background-color: #f4f4f4;
    text-align: center;
    margin: 0;
    padding: 0;
}

.background {
    position: fixed; /* Фиксируем фон */
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-image: url('images/Background.png');
    background-size: cover;
    background-position: center;
    z-index: -1; /* Помещаем фон под контент */
}

.quiz-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    background-color: #eca15182;
    max-width: 500px;
    margin: 50px auto;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

h1 {
    font-size: 26px;
    color: #333;
    margin-bottom: 20px;
}

#question {
    font-size: 20px;
    margin-top: 20px;
    color: #555;
}

#question-image {
    max-width: 100%;
    height: auto;
    margin-top: 20px;
    border-radius: 5px;
}

.options {
    display: flex;
    flex-direction: column;
    margin-top: 20px;
}

button {
    background-color: #007BFF;
    color: #fff;
    border: none;
    padding: 12px;
    margin-bottom: 15px;
    border-radius: 5px;
    cursor: pointer;
    transition: background-color 0.3s, transform 0.2s;
}

button:hover {
    background-color: #0056b3;
    transform: translateY(-2px);
}

#next-button {
    background-color: #28A745;
}

#next-button:hover {
    background-color: #218838;
}
```

Задача 6: Теперь script.js. И начнем мы его с массива, который положим в переменную. В массиве будут хранится данные для викторины:

```javascript
const questions = [
    {
        question: "Сколько планет в солнечной системе?",
        options: ["7", "8", "9"],
        correctAnswer: 1,
        image: "images/image1.jpg"
    },
    {
        question: "Какое наименьшее простое число?",
        options: ["0", "1", "2"],
        correctAnswer: 2,
        image: "images/image2.jpg"
    },
    {
        question: "Что символизирует красный цвет на светофоре?",
        options: ["Стоп", "Поехали", "Медленно"],
        correctAnswer: 0,
        image: "images/image3.jpg"
    }
];
```

Задача 7: Измените текст вопросов и ответы в соответствии с заготовленными вами. Добавьте еще 2 вопроса, учитывая структуру предыдущих вопросов. Продолжайте дальше писать в файле script.js.

Задача 8: Напишите логику действий викторины:

```javascript
let currentQuestion = 0;
let score = 0;

const questionText = document.getElementById("question");
const optionButtons = document.querySelectorAll(".options button");
const nextButton = document.getElementById("next-button");

function startQuiz() {
    questionText.innerText = questions[currentQuestion].question;

    const questionImage = document.getElementById("question-image");
    questionImage.src = questions[currentQuestion].image;
    questionImage.style.display = "block";

    optionButtons.forEach((button, index) => {
        button.innerText = questions[currentQuestion].options[index];
        button.addEventListener("click", () => checkAnswer(index));
    });
}

function checkAnswer(selectedIndex) {
    if (selectedIndex === questions[currentQuestion].correctAnswer) {
        score++;
    }

    currentQuestion++;

    if (currentQuestion < questions.length) {
        questionText.innerText = questions[currentQuestion].question;

        const questionImage = document.getElementById("question-image");
        questionImage.src = questions[currentQuestion].image;
        questionImage.style.display = "block";

        optionButtons.forEach((button, index) => {
            button.innerText = questions[currentQuestion].options[index];
        });
    } else {
        finishQuiz();
    }
}

function finishQuiz() {
    questionText.innerText = `Вы ответили правильно на ${score} из ${questions.length} вопросов.`;

    nextButton.style.display = "none";
}

nextButton.addEventListener("click", () => checkAnswer());

startQuiz();
```

*Задача 9: Добавьте еще 5 вопросов в викторину. Не забудьте про подготовку картинок, правильное их именование и то, что располагаться они должны в папке images. Также важно изменить и размер массива, добавив в него текст и путь новых вопросов.
