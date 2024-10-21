let currentQuestionIndex = 0;
let questions = [];

// Загрузка вопросов из JSON-файла
fetch('questions.json')
    .then(response => response.json())
    .then(data => {
        questions = data;
        showQuestion();
    });

function showQuestion() {
    const questionContainer = document.getElementById('question-container');
    const answersContainer = document.getElementById('answers-container');
    const nextButton = document.getElementById('next-button');

    // Очистка предыдущих ответов
    answersContainer.innerHTML = '';
    nextButton.classList.add('hidden');

    const currentQuestion = questions[currentQuestionIndex];
    
    // Установка изображения вопроса
    const questionImage = document.getElementById('question-image');
    questionImage.src = currentQuestion.image;

    // Создание кнопок ответов
    currentQuestion.answers.forEach((answer, index) => {
        const button = document.createElement('button');
        button.textContent = answer.text;
        button.classList.add('answer-button');
        button.onclick = () => selectAnswer(index);
        answersContainer.appendChild(button);
    });
}

function selectAnswer(index) {
    const currentQuestion = questions[currentQuestionIndex];
    const buttons = document.querySelectorAll('.answer-button');

    buttons.forEach((button, i) => {
        if (i === currentQuestion.correctAnswerIndex) {
            button.classList.add('correct');
        } else {
            button.classList.add('incorrect');
        }
        button.disabled = true; // Блокируем кнопки после выбора
    });

    document.getElementById('next-button').classList.remove('hidden');
}

document.getElementById('next-button').onclick = () => {
    currentQuestionIndex++;
    
    if (currentQuestionIndex < questions.length) {
        showQuestion();
    } else {
        alert('Вы завершили викторину!');
        // Можно добавить логику для перезапуска викторины или отображения результата
    }
};
