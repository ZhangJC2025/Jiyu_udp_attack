import http.server
import socketserver
import os

PORT = 8000

os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"正在共享当前文件夹")
    print("按 Ctrl+C 停止共享")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("停止共享")