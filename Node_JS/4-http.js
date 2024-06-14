const http = require('node:http');

const app = http.createServer((request, response) => {
    response.statusCode = 200;
    response.setHeader('Content-Type', 'text/plain');
    response.end('Hello Holberton School!')
})

const port = 1245;
app.listen(port, () => {
    console.log('...');
});

module.exports = app;
