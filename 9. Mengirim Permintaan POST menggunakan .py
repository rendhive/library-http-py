import http.client
import json

conn = http.client.HTTPConnection('httpbin.org')
payload = json.dumps({"name": "John", "age": 30})
headers = {'Content-Type': 'application/json'}

conn.request('POST', '/post', payload, headers)
response = conn.getresponse()
data = response.read()

print("Status:", response.status)
print("Response:", data.decode())
conn.close()
# Fungsi: Mengirimkan permintaan POST dengan payload JSON menggunakan HTTPConnection.
# Kondisi: Ketika Anda perlu mengirim data ke server.
