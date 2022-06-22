from Aula7_Televisão import Televisão
from Aula7_Calculadora1 import Calculadora
from Aula8_Conta_Letras import contador_letras
#Faz interações com outros arquivos.

if __name__ == '__main__':

    televisao = Televisão()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculdora = Calculadora(5, 5)
    print(calculdora.soma)
    lista = ['Cachorro', 'Gato', 'Elefante']
    print(contador_letras(lista))

#usado como o main de outras linguagens, ele deixa chamar o que está dentro dele apenas se estiver = a main!
# if __name__ == '__main__':
