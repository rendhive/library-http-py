from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Custom-Header', 'Value')
        self.end_headers()
        self.wfile.write(b'Check response headers.')

httpd = HTTPServer(('localhost', 8080), MyRequestHandler)
print("Server berjalan di http://localhost:8080")
httpd.serve_forever()
# Fungsi: Mengatur headers dalam response HTTP.
# Kondisi: Ketika Anda ingin menyediakan informasi tambahan dalam response.
