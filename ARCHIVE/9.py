import requests, json
from bs4 import BeautifulSoup as bp

# head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577'}
web = requests.get('https://blogunik.com/daftar-youtuber-indonesia-dengan-jumlah-subscriber-terbanyak/')
bs4 = bp(web.text, 'html.parser')
data = []

for jancok in bs4.find('div', class_='post-desc smaller-gap').findAll('h4'):
    text_besar = jancok.text
    data.append({'Nama dan Subsnya':text_besar})
print(json.dumps(data, indent=2, ensure_ascii=False))