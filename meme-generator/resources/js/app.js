import './bootstrap';

// resources/js/app.js

const dropArea = document.getElementById('memeForm');

dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropArea.style.border = '2px dashed #4CAF50';
});

dropArea.addEventListener('dragleave', () => {
    dropArea.style.border = '2px dashed #ccc';
});

dropArea.addEventListener('drop', (e) => {
    e.preventDefault();
    dropArea.style.border = '2px dashed #ccc';
    
    const file = e.dataTransfer.files[0];
    if (file && file.type.startsWith('image/')) {
        const reader = new FileReader();
        reader.onload = (event) => {
            document.getElementById('imageUpload').files = e.dataTransfer.files;
        };
        reader.readAsDataURL(file);
    }
});