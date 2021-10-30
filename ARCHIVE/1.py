import requests, json
from bs4 import BeautifulSoup as bp

data = []

page = 'https://quran.com'
web = requests.get(page)
semua_element = bp(web.text, 'html.parser')
x = 0
for quran in semua_element.findAll('div', class_='surah-card'):
    x = x + 1
    nama_surah = quran.h5.text
    arti_surah = quran.find('p', class_='english').text
    data.append({'No':x,'Surah':nama_surah,'Arti':arti_surah})
print(json.dumps(data, indent=2, ensure_ascii=False))
