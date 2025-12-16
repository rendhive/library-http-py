from http.server import HTTPServer, BaseHTTPRequestHandler

class CategoryHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/category1':
            self.send_response(200)
            self.wfile.write(b'Category 1 data')
        else:
            self.send_response(404)
            self.wfile.write(b'Category not found.')

httpd = HTTPServer(('localhost', 8082), CategoryHTTPRequestHandler)
print("Server berjalan di http://localhost:8082")
httpd.serve_forever()
# Fungsi: Mengelola beberapa kategori dalam server.
# Kondisi: Ketika Anda ingin menyajikan konten berdasarkan rute yang berbeda.
