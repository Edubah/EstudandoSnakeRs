contador_letras = lambda lista: [len(x) for x in lista]


lista_animais = ['Cachorro', 'Gato', 'Elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
print(soma(10, 10))

sub = lambda  a, b: a - b
print(sub(10, 5))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtração': lambda a, b: a - b,
    'multiplicação': lambda a, b: a * b,
    'divisão': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
multiplicacao = calculadora['multiplicação']

print(soma(10, 5))
print(multiplicacao(10, 9))