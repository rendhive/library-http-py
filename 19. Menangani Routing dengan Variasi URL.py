from http.server import HTTPServer, BaseHTTPRequestHandler

class RoutingHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.wfile.write(b'Homepage')
        elif self.path == '/about':
            self.send_response(200)
            self.wfile.write(b'About Page')
        else:
            self.send_response(404)
            self.wfile.write(b'Page not found')

httpd = HTTPServer(('localhost', 8085), RoutingHTTPRequestHandler)
print("Server berjalan di http://localhost:8085")
httpd.serve_forever()
# Fungsi: Membantu pengaturan route yang berbeda dalam server.
# Kondisi: Ketika Anda ingin mengelola beberapa halaman dalam aplikasi web.
