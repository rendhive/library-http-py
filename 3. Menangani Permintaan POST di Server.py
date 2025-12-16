from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # Dapatkan panjang konten
        post_data = self.rfile.read(content_length)  # Baca data
        print("Received POST data:", post_data.decode())
        self.send_response(200)
        self.end_headers()

httpd = HTTPServer(('localhost', 8080), MyRequestHandler)
print("Server berjalan di http://localhost:8080")
httpd.serve_forever()
# Fungsi: Menangani permintaan POST dan membaca data dari permintaan.
# Kondisi: Ketika Anda perlu menangani form submission atau data lain via POST.
