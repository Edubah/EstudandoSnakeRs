conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjunto_uniao = conjunto.union(conjunto2) #Une os conjuntos
print("União: ", conjunto_uniao)
conjunto_intersecao = conjunto.intersection(conjunto2) #Mostra a inteseção dos conjuntos
print("Interseção: ", conjunto_intersecao)
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(conjunto_diferenca1, " Diferença ", conjunto_diferenca2)
""""
conjunto = {1, 2, 3, 4, 5} #Declaração de Conjuntos
conjunto.add(6) #Adiciona elementos aos conjuntos
conjunto.discard(2) #Remove o número no conjunto
print(conjunto)
"""