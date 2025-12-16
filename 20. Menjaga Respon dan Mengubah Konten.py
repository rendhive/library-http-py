from http.server import HTTPServer, BaseHTTPRequestHandler

class ChangeContentHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Content has been changed!')

httpd = HTTPServer(('localhost', 8086), ChangeContentHandler)
print("Server berjalan di http://localhost:8086")
httpd.serve_forever()
# Fungsi: Mengubah dan menyajikan konten dinamis kepada pengguna.
# Kondisi: Ketika Anda perlu memberikan konten dinamis berdasarkan permintaan.
