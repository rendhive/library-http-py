import http.client
import urllib.parse

url = 'httpbin.org/get'
query_string = urllib.parse.urlencode({'name': 'John Doe', 'age': 30})

conn = http.client.HTTPConnection('httpbin.org')
conn.request('GET', f'{url}?{query_string}')
response = conn.getresponse()
print("Response:", response.read().decode())
conn.close()
# Fungsi: Menyusun dan mengirim permintaan dengan URL yang dikodekan.
# Kondisi: Ketika Anda perlu mengirim query string melalui URL.
