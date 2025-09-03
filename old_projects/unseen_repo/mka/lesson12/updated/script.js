function playClickSound() {
    const clickSound = document.getElementById("clickSound");
    clickSound.currentTime = 0;
    clickSound.play().catch(e => console.log("Не удалось воспроизвести звук:", e));
}

function appendToDisplay(value) {
    document.getElementById("display").value += value;
}

function clearDisplay() {
    document.getElementById("display").value = '';
}

function calculateResult() {
    const display = document.getElementById("display");
    try {
        display.value = eval(display.value);
    } catch (error) {
        display.value = 'Ошибка';
        setTimeout(clearDisplay, 1500);
    }
}

function handleButtonClick(value) {
    playClickSound();
    
    if (value === 'C') {
        clearDisplay();
    } else if (value === '=') {
        calculateResult();
    } else {
        appendToDisplay(value);
    }
}

document.addEventListener('keydown', function(event) {
    const key = event.key;
    const validKeys = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/','=','Enter','c','C','.'];
    
    if (validKeys.includes(key)) {
        playClickSound();
        
        if (key === 'Enter') {
            calculateResult();
        } else if (key.toLowerCase() === 'c') {
            clearDisplay();
        } else if (key === '=') {
            calculateResult();
        } else {
            appendToDisplay(key);
        }
    }
});