import http.client
import base64

conn = http.client.HTTPConnection('httpbin.org')
credentials = f'user:passwd'
encoded_credentials = base64.b64encode(credentials.encode()).decode()
headers = {'Authorization': 'Basic ' + encoded_credentials}

conn.request('GET', '/basic-auth/user/passwd', headers=headers)
response = conn.getresponse()

print("Status:", response.status)
print("Response:", response.read().decode())
conn.close()
# Fungsi: Mengirim permintaan untuk mengakses endpoint yang dilindungi otentikasi.
# Kondisi: Ketika Anda perlu mengakses resource yang membutuhkan otentikasi.
