import requests, re, time
from bs4 import BeautifulSoup

def scrapekompas(ambil_berita:int):
    try:
        _kompas = requests.get('https://www.kompas.com/')
        _cvbs4 = BeautifulSoup(_kompas.content, 'html.parser')

        _findel = _cvbs4.find('div',{'class','most__wrap clearfix'})

        _findtitle = re.findall('<h4 class="most__title">(.*?)</h4>', str(_findel))[ambil_berita]
        _findlink = re.findall('<a class="most__link" href="(.*?)"', str(_findel))[ambil_berita]
        _findpembaca = re.findall('<div class="most__read">(.*?)</div>', str(_findel))[ambil_berita]
        return f'Title: {_findtitle}\nLink: {_findlink}\nKeterangan: {_findpembaca}'
    except:
        pass

if __name__ == '__main__':
    print('='*25)
    print('Kompas Scraper by iFanpS\nUntuk berita populer saja')
    print('='*25)
    time.sleep(2)
    try:
        print('Berita populer yang selalu tersedia 9')
        _angka = int(input('Masukan nomor berita 0-9: '))
        print(f'Berita yang anda cari:\n{scrapekompas(_angka)}')
    except ConnectionError:
        print('Periksa koneksi anda!')
    except:
        print('Berita tidak ditemukan!')