import http.client
import json

conn = http.client.HTTPConnection('jsonplaceholder.typicode.com')
conn.request('GET', '/posts/1')
response = conn.getresponse()
data = response.read()
json_data = json.loads(data)

print("Title:", json_data['title'])
conn.close()
# Fungsi: Mengambil data dalam format JSON dari API dan memparsingnya.
# Kondisi: Ketika Anda perlu mendapatkan informasi dalam format JSON.
