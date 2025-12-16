import http.client

connection = http.client.HTTPConnection('www.example.com')
connection.request('GET', '/')
response = connection.getresponse()

print("Status:", response.status)
print("Response:", response.read(100))  # Mengambil 100 karakter pertama dari respons
connection.close()
# Fungsi: Mengirim permintaan HTTP menggunakan HTTPConnection.
# Kondisi: Ketika Anda ingin mengambil data dari URL dengan kontrol penuh atas permintaan.
