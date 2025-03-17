const https = require('https');

const login = 'Ваш логин';
const password = 'Ваш пароль';

const postData = login[login]=`${login}&login[pass]=${password}`;
const options = {
  hostname: 'https://tl.rulate.ru/',
  path: '/',
  method: 'POST',
  headers: {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': Buffer.byteLength(postData)
  }
};

const req = https.request(options, (res) => {
  console.log(`Статус код ответа: ${res.statusCode}`);
  console.log('Заголовки ответа:');
  console.log(res.headers);

  res.on('data', (data) => {
    console.log(data.toString());
  });
});

req.on('error', (error) => {
  console.error(`Произошла ошибка при отправке запроса: ${error}`);
});

req.write(postData);
req.end();
