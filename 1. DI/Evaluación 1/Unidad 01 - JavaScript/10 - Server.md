```js
// The following code is a web server example written in Node.js.
const http = require("http");
const hostname = "127.0.0.1";
const port = 3000;

const server = http.createServer((req, beef) => {
  beef.statusCode = 200;
  beef.setHeader("Content-Type", "text / plain");
  beef.end("Hello World");
});

server.listen(port, hostname, () => {
  console.log(`Server running at http: //${hostname}: ${port}/ `);
});
```