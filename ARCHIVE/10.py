import requests, json, re
from bs4 import BeautifulSoup as bp

list = []
try:
    isi_isi_negara = requests.get('https://www.worldometers.info/coronavirus/#countries')
    lihat = bp(isi_isi_negara.text, 'html.parser')
    for nama_negaras in lihat.findAll('a', class_='mt_a'):
        list.append(nama_negaras.text)
except ConnectionError:
    print('Koneksi tidak terdeteksi')
except ConnectionAbortedError:
    print('Menghentikan program perihal koneksi buruk!')
except TimeoutError:
    print('TimeOut error terjadi')
    
data = []
nama_negara = input('Masukan negara yang ingin di cari\n>> ')
nama_negara_hrfbsr = nama_negara.title()
if nama_negara_hrfbsr in list:
    web = requests.get('https://www.worldometers.info/coronavirus/country/{0}/'.format(nama_negara))
    cvrt = bp(web.text, 'html.parser')
    data1 = re.findall('<span style="color:#aaa">(.*?) </span>', str(cvrt))[0]
    data2 = re.findall('<span>(.*?)</span>', str(cvrt))[0]
    data3 = re.findall('<span>(.*?)</span>', str(cvrt))[1]
    data.append({'Negara':nama_negara,'Total kasus':data1,'Total kematian':data2,'Total sembuh':data3})
    print(json.dumps(data, indent=2, ensure_ascii=False))
else:
    print('Negara tidak ditemukan')
    exit()