from http.server import HTTPServer, BaseHTTPRequestHandler

class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Welcome to my server!')
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Page not found')

httpd = HTTPServer(('localhost', 8080), MyRequestHandler)
print("Server berjalan di http://localhost:8080")
httpd.serve_forever()
# Fungsi: Menangani berbagai rute dalam permintaan GET pada server.
# Kondisi: Ketika Anda ingin mengelola berbagai endpoint dalam aplikasi server Anda.
