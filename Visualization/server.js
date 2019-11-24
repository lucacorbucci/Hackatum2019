const fs = require('fs');
var jsonlint = require("jsonlint");

const server = require('http').createServer(function (req, res) {
  // Set CORS headers
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Request-Method', '*');
  res.setHeader('Access-Control-Allow-Methods', 'OPTIONS, GET');
  res.setHeader('Access-Control-Allow-Headers', '*');
  if (req.method === 'OPTIONS') {
    res.writeHead(200);
    res.end();
    return;
  }
});

server.on('request', (req, res) => {
  try {
    const src = fs.createReadStream('./data.json');
    src.pipe(res);
  }
  catch (e) {

  }

});

server.listen(8000);
