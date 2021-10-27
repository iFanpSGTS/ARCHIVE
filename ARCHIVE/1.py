import requests, json
from bs4 import BeautifulSoup as bp

data = []

page = 'https://quran.com'
web = requests.get(page)
semua_element = bp(web.text, 'html.parser')

for quran in semua_element.findAll('div', class_='surah-card'):
    nama_surah = quran.h5.text
    arti_surah = quran.find('p', class_='english').text
    data.append({'Surah':nama_surah,'Arti':arti_surah})
dumpin = json.dumps(data, indent=2, ensure_ascii=False)
with open('hasil_surah.json','w') as surah_write:
    surah_write.write(dumpin)
    surah_write.close()