#Função é tudo aquilo que retorna valor, Métodos já não retornam!

#def = forma como é declarado um método, sempre acompanhado de um nome com letras minúsculas.
#class = Forma como é declarado uma classe. Por convenção, classe começa com letra maiúscula.

class Calculadora:

    def soma (self, a, b):
        return a + b

    def sub (self, a, b):
        return a - b

    def mult (self, a, b):
        return a * b

    def div(self, a, b):
        return a / b

calculadora = Calculadora()
print(calculadora.soma(10, 5))
print(calculadora.sub(12, 6))
print(calculadora.mult(100, 15))
print(calculadora.div(100, 2))