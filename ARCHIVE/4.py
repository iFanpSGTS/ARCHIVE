from bs4 import BeautifulSoup as bp
import requests, re

try:
    web = 'https://www.merdeka.com/gaya/100-peribahasa-indonesia-populer-dan-artinya.html'

    web_req = requests.get(web)

    web_scrape = bp(web_req.text, 'html.parser')

    h2_pribahasa_arti = web_scrape.select('h2')

    p_isian_pribahasa = web_scrape.select('p')

    p_search = '\n'.join([ p.text for p in p_isian_pribahasa[4:210] ])
    h2_search = ''.join([ h2.text for h2 in h2_pribahasa_arti[0:1] ])

    with open('pribahasa_arti.txt','a+') as pr:
        pr.write(f'{h2_search}\n{p_search}')

    f1 = open('pribahasa_arti.txt','r').read()
    change_ab = re.findall('1. (.*?) Peribahasa dan Artinya', str(h2_search))[0]

    change = f1.replace(change_ab, '(A-T)')
    f2 = open('pribahasa_arti.txt','w')
    f2.write(change)
    f2.close()

except:
    print('Jalankan ulang program, atau nyalakan wifi anda!')