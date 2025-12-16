from http.server import SimpleHTTPRequestHandler, HTTPServer

httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
print("Server static berjalan di http://localhost:8080")
httpd.serve_forever()
# Fungsi: Menyajikan file statis menggunakan SimpleHTTPRequestHandler.
# Kondisi: Ketika Anda ingin melayani file seperti HTML, CSS, atau gambar.
