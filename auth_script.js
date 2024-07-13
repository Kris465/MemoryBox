const https = require('https');

// Ваши учетные данные
const login = 'Ваш логин';
const password = 'Ваш пароль';

// Данные для POST запроса
const postData = login[login]=${login}&login[pass]=${password};
const options = {
  hostname: 'https://tl.rulate.ru/',
  path: '/',
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': Buffer.byteLength(postData)
  }
};

// Отправка POST запроса
const req = https.request(options, (res) => {
  console.log(Статус код ответа: ${res.statusCode});
  console.log('Заголовки ответа:');
  console.log(res.headers);

  // Обработка данных ответа, если необходимо
  res.on('data', (data) => {
    console.log(data.toString());
  });
});

req.on('error', (error) => {
  console.error(Произошла ошибка при отправке запроса: ${error});
});

// Отправка данных
req.write(postData);
req.end();
