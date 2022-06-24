import random, string

tamanho = int(input('Digite o tamanho de senha que você deseja: £'))

chars = string.ascii_letters + string.digits + '!@#$%&*(ç)-=+,.:;/?'

rnd = random.SystemRandom() #Biblioteca OS com a classe URANDOM

#Rnd.Choice retorna uma lista com caracteres randômicos
print(''.join(rnd.choice(chars) for i in range(tamanho)))