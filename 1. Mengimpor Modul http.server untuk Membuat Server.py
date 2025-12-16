from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)  # Send response code
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b"Hello, World!")  # Send response body

httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
print("Server berjalan di http://localhost:8080")
httpd.serve_forever()  # Fungsi: Membuat server HTTP sederhana dengan handler.
# Kondisi: Ketika Anda ingin membuat server lokal untuk melayani permintaan HTTP.
