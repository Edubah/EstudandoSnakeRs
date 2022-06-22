#Função é tudo aquilo que retorna valor, Métodos já não retornam!

#def = forma como é declarado um método, sempre acompanhado de um nome com letras minúsculas.
#class = Forma como é declarado uma classe. Por convenção, classe começa com letra maiúscula.

class Calculadora:
    def __init__(self, num1, num2):
        self.a = num1
        self.b = num2

    def soma (self):
        return self.a + self.b

    def sub (self):
        return self.a - self.b

    def mult (self):
        return self.a * self.b

    def div(self):
        return self.a / self.b

if __name__ == '__main__':

    calculadora = Calculadora(10, 2)
    print(calculadora.a)
    print(calculadora.soma())
    print(calculadora.sub())
    print(calculadora.mult())
    print(calculadora.div())