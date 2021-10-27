from bs4 import BeautifulSoup
import requests, json

#Cari daerahnya
try:
    daerahnya = json.loads(open('daerah.json','r').read())
    daerah = input('Masukan daerahmu: ')
    daerah = daerah.title()
    if daerah in daerahnya.keys():
        web =  requests.get('https://www.jadwalsholat.org/adzan/monthly.php?id={0}'.format(daerahnya[daerah]))
        scrape_web = BeautifulSoup(web.text, 'html.parser')

    #Cari real time
        cari_waktu = scrape_web.find('tr', class_='table_highlight').findAll('td')[1:]
        waktu = ''.join([ wkt.text for wkt in cari_waktu ])
        # print(waktu)
        print(f'Imsyak: {waktu[0:5]}\nSubuh: {waktu[5:10]}\nTerbit: {waktu[10:15]}\nDhuha: {waktu[15:20]}\nDzuhur: {waktu[20:25]}\nAshar: {waktu[25:30]}\nMaghrib: {waktu[30:35]}\nIsya: {waktu[35:40]}')
except Exception as e:
    print(e)