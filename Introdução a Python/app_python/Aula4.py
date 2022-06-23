

""""
a = int(input("Entre com um valor: "))
for num in range(a):
    div = 0
    for x in range(1, num+1): #Para x que percorre de 1 a "a" + 1 - faça
        resto = num % x #Resto recebe resto da divisão entre a e x
        #print('Dividido por: ', x, 'Restou: ', resto)
        if resto == 0: #Se resto for igual a 0
            div = div + 1 #variável "div" recebe ela mesma +1

    if div == 2:
        print(num)

"""

""""
a = int(input("Entre com um número: "))

div = 0
for x in range(1, a + 1): #Para x que percorre de 1 a "a" + 1 - faça
    resto = a % x #Resto recebe resto da divisão entre a e x
    print('Dividido por: ', x, 'Restou: ', resto)
    if resto == 0: #Se resto for igual a 0
        div = div + 1 #variável "div" recebe ela mesma +1

if div == 2:
    print('Número {} é primo'.format(a))
else:
    print('número {} não é primo'.format(a))
"""
