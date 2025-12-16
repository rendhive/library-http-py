from http.server import HTTPServer, BaseHTTPRequestHandler

class MultiClientHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Multi client test.')

httpd = HTTPServer(('localhost', 8083), MultiClientHandler)
print("Server mendengarkan di http://localhost:8083")
httpd.serve_forever()
# Fungsi: Melayani lebih dari satu klien dengan server HTTP.
# Kondisi: Ketika Anda ingin mengelola permintaan bersamaan dari banyak klien.
