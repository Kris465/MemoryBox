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
