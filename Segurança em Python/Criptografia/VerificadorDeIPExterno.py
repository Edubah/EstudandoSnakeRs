import re
import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
# host_name = dados['hostname']
# cid = dados['city']
pais = dados['country']
# postal = dados['postal']
# loc = dados['loc']

print('Detalhes do IP externo\n')
print('IP {0}\nPaís: {1}'.format(ip, pais))