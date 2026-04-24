/**
 * Терминальные обои с имитацией vim/nano
 */

// Конфигурация
const CONFIG = {
    TYPING_SPEED: 1000,
    FILE_CHANGE_DELAY: 3000,
    SHOW_LINE_NUMBERS: true,
    MAX_CHARS: 3000,
};

let currentFileIndex = -1;
let typingInterval = null;
let isTyping = false;
let currentLine = 1;
let currentColumn = 1;

function getRandomFileIndex() {
    if (!CODE_FILES || CODE_FILES.length === 0) return -1;
    if (CODE_FILES.length === 1) return 0;
    let newIndex;
    do {
        newIndex = Math.floor(Math.random() * CODE_FILES.length);
    } while (newIndex === currentFileIndex && CODE_FILES.length > 1);
    return newIndex;
}

function updatePosition(char) {
    if (char === '\n') {
        currentLine++;
        currentColumn = 1;
    } else {
        currentColumn++;
    }
    const posEl = document.getElementById('position');
    if (posEl) posEl.textContent = currentLine + ':' + currentColumn;
}

function updateLineNumbers(totalLines) {
    const lineNumbersEl = document.getElementById('lineNumbers');
    if (!lineNumbersEl) return;
    
    let html = '';
    for (let i = 1; i <= totalLines; i++) {
        html += '<div>' + i + '</div>';
    }
    lineNumbersEl.innerHTML = html;
}

function updateProgress(current, total) {
    const progressEl = document.getElementById('fileProgress');
    if (!progressEl) return;
    progressEl.textContent = Math.round((current / total) * 100) + '%';
}

function updateClock() {
    const now = new Date();
    const clockEl = document.getElementById('clock');
    if (clockEl) clockEl.textContent = 
        String(now.getHours()).padStart(2, '0') + ':' + 
        String(now.getMinutes()).padStart(2, '0');
}

function typeCode(content, element) {
    return new Promise((resolve) => {
        if (content.length > CONFIG.MAX_CHARS) {
            content = content.substring(0, CONFIG.MAX_CHARS) + '\n\n... (обрезано)';
        }
        
        const chars = content.split('');
        let charIndex = 0;
        let output = '';
        
        isTyping = true;
        currentLine = 1;
        currentColumn = 1;
        
        const totalLines = (content.match(/\n/g) || []).length + 1;
        updateLineNumbers(totalLines);
        
        // Создаём курсор внутри элемента
        const cursor = document.createElement('span');
        cursor.className = 'cursor';
        cursor.id = 'cursor';
        
        // Находим контейнер для прокрутки
        const codeArea = document.querySelector('.code-area');
        
        function typeNextChar() {
            if (charIndex >= chars.length) {
                isTyping = false;
                resolve();
                return;
            }
            
            const char = chars[charIndex];
            output += char;
            element.textContent = output;
            element.appendChild(cursor);
            
            // Плавная прокрутка вниз
            if (codeArea) {
                codeArea.scrollTop = codeArea.scrollHeight;
            }
            
            updatePosition(char);
            updateProgress(charIndex + 1, chars.length);
            
            charIndex++;
            
            const delay = Math.max(5, CONFIG.TYPING_SPEED + Math.random() * 10 - 5);
            typingInterval = setTimeout(typeNextChar, delay);
        }
        
        typeNextChar();
    });
}

async function showFile(fileIndex) {
    if (fileIndex < 0 || fileIndex >= CODE_FILES.length) return;
    
    if (typingInterval) {
        clearTimeout(typingInterval);
        typingInterval = null;
    }
    
    const file = CODE_FILES[fileIndex];
    const codeElement = document.getElementById('codeContent');
    const filePathElement = document.getElementById('filePath');
    const languageBadge = document.getElementById('languageBadge');
    const vimStatus = document.getElementById('vimStatus');
    const terminalMode = document.getElementById('terminalMode');
    
    if (!codeElement) return;
    
    currentLine = 1;
    currentColumn = 1;
    updatePosition('');
    updateProgress(0, 100);
    
    if (filePathElement) filePathElement.textContent = file.path;
    if (languageBadge) languageBadge.textContent = file.language.toUpperCase();
    if (vimStatus) {
        vimStatus.textContent = '-- INSERT --';
        vimStatus.style.color = '#238636';
    }
    if (terminalMode) {
        terminalMode.textContent = 'INSERT';
        terminalMode.style.background = '#238636';
    }
    
    codeElement.textContent = '';
    
    await typeCode(file.content, codeElement);
    
    if (vimStatus) {
        vimStatus.textContent = '-- NORMAL --';
        vimStatus.style.color = '#f0883e';
    }
    if (terminalMode) {
        terminalMode.textContent = 'NORMAL';
        terminalMode.style.background = '#f0883e';
    }
    
    setTimeout(() => {
        if (!isTyping) {
            showFile(getRandomFileIndex());
        }
    }, CONFIG.FILE_CHANGE_DELAY);
}

function init() {
    if (!CODE_FILES || CODE_FILES.length === 0) return;
    
    updateClock();
    setInterval(updateClock, 1000);
    
    const firstIndex = getRandomFileIndex();
    currentFileIndex = firstIndex;
    showFile(firstIndex);
}

// Запуск
if (typeof CODE_FILES !== 'undefined' && CODE_FILES.length > 0) {
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
}
