from math import prod
from urllib.error import ContentTooShortError
import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_consulta = []

url = 'https://lista.mercadolivre.com.br/'

produto = input('Qual é o produto que você deseja?')

response = requests.get(url+produto)

content = response.content

site = BeautifulSoup(content, 'html.parser')

consulta = site.findAll('div', attrs={'class': 'ui-search-result__wrapper'})

for produtos in consulta:
    titulo = produtos.find('h2', attrs={'class': 'ui-search-item__title ui-search-item__group__element'})
    valor = produtos.find('span', attrs={'class', 'price-tag-amount'})
    link = produtos.find('a', attrs={'class': 'ui-search-link'})

    lista_consulta.append([titulo.text, valor.text, link['href']])
    print(titulo.text)
    print(valor.text)
    print(link['href'])
    print()

produtos_lista = pd.DataFrame(lista_consulta, columns=['Título', 'Valor', 'Link'])
produtos_lista.to_excel('find-ml.xlsx', index=False)
#print(produtos_lista)