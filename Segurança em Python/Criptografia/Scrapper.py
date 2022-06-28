from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content
#Objeto site receberá o conteúdo da requisição http do site
soup = BeautifulSoup(site, 'html.parser')
#Objeto soup está baixando do site HTML
#print(soup.prettify())
#PRETTIFY - Transforma o HTML em string

