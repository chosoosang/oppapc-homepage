#!/usr/bin/env python3
"""
오빠피씨 직업소개소 정적 파일 서버
포트: 8767
"""
import http.server
import socketserver
import os

PORT = 8767
DIRECTORY = "/home/joeun/oppapc-homepage/agency"

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-cache')
        super().end_headers()

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("127.0.0.1", PORT), Handler) as httpd:
        print(f"직업소개소 서버 시작: http://127.0.0.1:{PORT}")
        httpd.serve_forever()
