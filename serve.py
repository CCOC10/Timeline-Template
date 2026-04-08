#!/usr/bin/env python3
import http.server
import os

DIRECTORY = os.path.expanduser("~/timeline-new")
PORT = 8080

os.chdir(DIRECTORY)

handler = http.server.SimpleHTTPRequestHandler
with http.server.HTTPServer(("", PORT), handler) as httpd:
    print(f"Serving on http://localhost:{PORT}")
    httpd.serve_forever()
