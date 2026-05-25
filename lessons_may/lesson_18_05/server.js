// const http = require("http");
// const fs = require("fs");
// const { error } = require("console");

// http
//   .createServer((request, response) => {
//     let filePath = request.url.substring(1);
//     if (!filePath) filePath = "index.html";
//     response.setHeader("Content-Type", "text/html; charset=utf-8;");
//     fs.readFile(filePath, (error, data) => {
//       if (error) {
//         response.statusCode = 404;
//         response.end("<h1>Запрашиваемый ресурс не найден</h1>");
//       } else {
//         response.end(data);
//       }
//     });
//   })
//   .listen(666, () =>
//     console.log("Сервер запущен по адресу http://localhost:222"),
//   );


const http = require("http");
const fs = require("fs");
const { error } = require("console");

http
  .createServer((request, response) => {
    if(request.url == "/data"){
      fs.readFile("data.json", (_, data) => response.end(data));
    } else{
      fs.readFile("index.html", (_, data) => response.end(data));
    }
  }).listen(222, () =>
    console.log("Сервер запущен по адресу http://localhost:222"),
  );