from http.server import HTTPServer, BaseHTTPRequestHandler

class DebugHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(f"Request received: {self.path}")
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(b'Debugging information logged.')

httpd = HTTPServer(('localhost', 8081), DebugHTTPRequestHandler)
print("Listening on http://localhost:8081")
httpd.serve_forever()
# Fungsi: Merekam informasi debugging untuk setiap permintaan yang masuk.
# Kondisi: Ketika Anda ingin melacak permintaan untuk analisis atau dekode masalah.
