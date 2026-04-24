const questions = [
    { question: "Какой язык программирования используется для веб-разработки?", answers: ["Python", "JavaScript", "Java"], correct: 1 },
    { question: "Какой из этих фреймворков используется для разработки на JavaScript?", answers: ["Django", "React", "Spring"], correct: 1 },
    { question: "Что такое CSS?", answers: ["Язык разметки", "Язык стилей", "Язык программирования"], correct: 1 }
];

let currentQuestionIndex = 0, score = 0;

function showQuestion() {
    const q = questions[currentQuestionIndex];
    document.getElementById('question-container').innerText = q.question;
    
    const buttons = document.getElementById('answer-buttons');
    buttons.innerHTML = '';
    
    q.answers.forEach((answer, index) => {
        const button = document.createElement('button');
        button.innerText = answer;
        button.className = 'btn';
        button.onclick = () => selectAnswer(index === q.correct);
        buttons.appendChild(button);
    });
}

function selectAnswer(correct) {
    if (correct) score += 2;
    currentQuestionIndex++;
    
    if (currentQuestionIndex < questions.length) {
        document.getElementById('next-button').style.display = 'block';
        showQuestion();
    } else {
        showResult();
    }
}

function showResult() {
    document.getElementById('question-container').style.display = 'none';
    document.getElementById('answer-buttons').style.display = 'none';
    document.getElementById('next-button').style.display = 'none';
    
    document.getElementById('result-container').style.display = 'block';
    document.getElementById('score').innerText = score;
}

document.getElementById('next-button').onclick = showQuestion;

showQuestion();