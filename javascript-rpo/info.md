Установка:
```bash
npm init -y
```
```bash
   npm install prompt-sync
```
Пример:
```bash
   const prompt = require('prompt-sync')();
   
   const name = prompt('Введите ваше имя: ');
   console.log(`Привет, ${name}!`);
```

