import requests
from bs4 import BeautifulSoup as bp
import pandas as tabels

data = []

page = requests.get('https://www.brilio.net/wow/40-kata-kata-keren-quotes-cocok-dijadikan-caption-medsosmu-191127s.html')
soup = bp(page.text, 'html.parser')

h2_judul = soup.select('h2')
p_isi = soup.select('p')

judul = '\n'.join([ h.text for h in h2_judul[1:] ])
isian = '\n'.join([ p.text for p in p_isi[16:146] ])

data.append({
    'Judul': judul,
    'Isian': isian
})

tabel = tabels.DataFrame(data)

tabel.to_csv('indo_quote.csv', index=False, encoding='utf-8')
#########################################################################################################################################

for page in range(1,11): # di pakai untuk randomize page

    if page == 1: 
        url = "http://quotes.toscrape.com"
    else: 
        url = "http://quotes.toscrape.com/page/"+str(page)

    page = requests.get(url) # request get tipe ke urlnya
    soup = bp(page.content, 'html.parser') # ambil page content nya (isiannya, element maksud saya)

    quotes = soup.find_all('div', class_='quote') # cari element bagian quotes
    
    for q in quotes:
        quote = q.find('span', class_='text').text
        author = q.find('small', class_='author').text

        tag = q.find('div', class_='tags')  # ini semua adalah bagian untuk ngambil quote, author, tag
        # tags = [tag.text for tag in q.find('div', class_='tags').find_all('a', class_='tag')]
        tags = tag.select('a')
        tags = ''.join([ t.text for t in tags ])

        with open('quote.txt', 'a+') as _write:
            _write.write(f'\n Quotenya:\n{quote}\n Author: {author}\n Tagsnya:\n {tags}')