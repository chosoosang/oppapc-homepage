#!/usr/bin/env python3
import http.server, socketserver, os

PORT = 8767
DIRECTORY = "/home/joeun/oppapc-homepage/agency"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    def do_GET(self):
        if self.path == '/':
            self.send_response(302)
            self.send_header('Location', '/jobagency_personal.html')
            self.end_headers()
            return
        super().do_GET()
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()
    def log_message(self, format, *args): pass

class ReuseAddrServer(socketserver.TCPServer):
    allow_reuse_address = True

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with ReuseAddrServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"서버 시작: http://127.0.0.1:{PORT}")
        httpd.serve_forever()
