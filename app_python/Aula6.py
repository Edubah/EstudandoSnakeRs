conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2) #Une os conjuntos
print('União: {}'.format(conjunto_uniao))

conjunto_intersecao = conjunto.intersection(conjunto2) #Mostra a inteseção dos conjuntos
print('Interseção: {}'.format(conjunto_intersecao))

conjunto_diferenca1 = conjunto.difference(conjunto2) #Mostra a diferença entre os conjuntos
conjunto_diferenca2 = conjunto2.difference(conjunto)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}'.format(conjunto_diferenca2))

conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2) #Mostra o que não tem em ambos os conjuntos
print('Diferença Simétrica: {}'.format(conjunto_dif_simetrica))

lista = ['cahcorro', 'cachorro', 'gato', 'gato', ' elefante']
print(lista)
conjunto_animais = set(lista) #Retira a duplicidade
print(conjunto_animais)

lista_animais = list(conjunto_animais) #Volta a ser uma lista
print(lista_animais)
""""
conjunto = {1, 2, 3, 4, 5} #Declaração de Conjuntos
conjunto.add(6) #Adiciona elementos aos conjuntos
conjunto.discard(2) #Remove o número no conjunto
print(conjunto)
"""