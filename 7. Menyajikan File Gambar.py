from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/image':
            self.send_response(200)
            self.send_header('Content-Type', 'image/png')
            self.end_headers()
            with open('example.png', 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_response(404)
            self.end_headers()

httpd = HTTPServer(('localhost', 8080), MyRequestHandler)
print("Server berjalan di http://localhost:8080")
httpd.serve_forever()
# Fungsi: Menyajikan file gambar melalui HTTP.
# Kondisi: Ketika Anda ingin menampilkan gambar sebagai bagian dari response.
