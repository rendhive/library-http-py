from http.server import HTTPServer, BaseHTTPRequestHandler

class XMLHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'application/xml')
        self.end_headers()
        self.wfile.write(b'<response><message>Hello, XML!</message></response>')

httpd = HTTPServer(('localhost', 8084), XMLHTTPRequestHandler)
print("Server berjalan di http://localhost:8084")
httpd.serve_forever()
# Fungsi: Menyajikan data dalam format XML.
# Kondisi: Ketika Anda perlu memberikan response dalam format XML.
