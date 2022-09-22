from turtle import clear
from xml.sax.xmlreader import AttributesImpl
import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com/')
content = response.content
site = BeautifulSoup(content, 'html.parser')

# html da noticia
noticias = site.findAll('div', attrs={'class': 'feed-post'})

for noticia in noticias:
    # titulo
    titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
    print(titulo.text)
    # salvar a lista em uma tabela
    lista_noticias.append([titulo.text, titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Título', 'Link'])
news.to_excel('find_news-g1-noticias.xlsx', index=False)
#print(news)