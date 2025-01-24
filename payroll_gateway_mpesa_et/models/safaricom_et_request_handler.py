import json
from functools import cached_property
from http.cookies import SimpleCookie
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse

class SafaricomEtRequestHandler(BaseHTTPRequestHandler):
    # ...

    def do_POST(self):

        self.send_response_only(200)
        content_len = int(self.headers.getheader('content-length', 0))
        post_body = self.rfile.read(content_len)

def run(server_class=HTTPServer, handler_class=SafaricomEtRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()