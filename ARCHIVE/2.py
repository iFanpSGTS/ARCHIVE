import requests, json
from bs4 import BeautifulSoup as bp

req = requests.get('https://www.bmkg.go.id/warning.bmkg')
req_content = bp(req.text, 'html.parser').findAll('section')[1]

lokasi_gempa = req_content.find('div', class_='col-12').findAll('p')

info = ''.join(lokasi_gempa[0].text)
lokasi = ''.join(lokasi_gempa[1].text)
arahan = ''.join(lokasi_gempa[2].text)
saran = ''.join(lokasi_gempa[3].text)

waktu_pemutakhiran = req_content.find('div', class_='row').findAll('small')
wktp = ''.join(waktu_pemutakhiran[0].text).replace('—', '')

data = ({
    'Info':info,
    'Lokasi':lokasi,
    'Arahan':arahan,
    'Saran':saran,
    'Waktu Pemutakhiran':wktp
})

print(json.dumps(data, indent=2, ensure_ascii=False))