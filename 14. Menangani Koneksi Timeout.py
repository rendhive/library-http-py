import http.client

conn = http.client.HTTPConnection('httpbin.org', timeout=1)  # Timeout diatur
try:
    conn.request('GET', '/')
    response = conn.getresponse()
    print("Response Status:", response.status)
except Exception as e:
    print("Error:", e)
# Fungsi: Mengatur batas waktu untuk koneksi dan menangani potensi timeout.
# Kondisi: Ketika Anda ingin memastikan bahwa server merespons dalam waktu tertentu.
