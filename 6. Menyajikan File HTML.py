from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Hello, World!</h1></body></html>')

httpd = HTTPServer(('localhost', 8080), MyRequestHandler)
print("Server berjalan di http://localhost:8080")
httpd.serve_forever()
# Fungsi: Menyajikan konten HTML melalui server.
# Kondisi: Ketika Anda ingin memberikan tampilan halaman web.
