import json
import random
import requests

from domonic.html import *

from http.server import BaseHTTPRequestHandler
from helpers import http_server


# urllib3 for url parse

class BookHandler(BaseHTTPRequestHandler):
    # Handler for the GET random number info
    def do_GET(self):
        print('Get request received')
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        resp = requests.get(f"http://numbersapi.com/{random.randint(0, 100)}")
        mydom = html(
            body(
                div(resp.content.decode(), _style="color:green; font-size:20px;"),
                img(_src="https://github.githubassets.com/apple-touch-icon-114x114.png"),
                h1(resp.content.decode())
            )
        )
        render(mydom)
        self.wfile.write(f"{mydom}".encode())

if _name_ == "_main_":
    server = http_server.Server(handler=BookHandler)
    server.run()
