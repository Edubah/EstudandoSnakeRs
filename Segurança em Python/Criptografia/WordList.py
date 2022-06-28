import itertools

string = input('String a ser permutada: ')
resultado = itertools.permutations(string, len(string)) #Fará a permutação das palavras

for i in resultado:
    print(''.join(i))