var http = require('http');

http.createServer(function (req, res) {
  if( req.url === "/debug")
{
res.writeHead(200, {'Content-Type': 'text/plain'});
res.end("success"+req.url);
}
else
{
res.writeHead(200, {'Content-Type': 'text/plain'});
res.end("failed"+req.url);
}

}).listen(3000);
