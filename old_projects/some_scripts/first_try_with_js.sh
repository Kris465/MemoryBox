#!/bin/bash

# Устанавливаем Node.js для выполнения JavaScript кода
NODE_CODE=$(cat <<EOF
const https = require('https');

const postData = JSON.stringify({
  key1: 'value1',
  key2: 'value2'
});

const options = {
  hostname: 'www.example.com',
  port: 443,
  path: '/api/endpoint',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': postData.length
  }
};

const req = https.request(options, (res) => {
  console.log('statusCode:', res.statusCode);
  console.log('headers:', res.headers);

  res.on('data', (d) => {
    process.stdout.write(d);
  });
});

req.on('error', (e) => {
  console.error(e);
});

req.write(postData);
req.end();
EOF
)

# Выполняем JavaScript код с помощью Node.js
echo "$NODE_CODE" | node
