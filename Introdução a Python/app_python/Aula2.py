a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
soma = a + b
sub = a - b
mult = a * b
div = a / b
resto = a % b


#Convertendo no python
#[tipo](variável) - Ex: str(soma) < - Simples

#print('Soma ()') [format](variável) - Ex: print('Soma: ()'.format(soma) <- foma geral e mais utilizada.
print (soma)
print (sub)
print (mult)
print (div)
print (resto)

print('Soma: {soma} \nSubtração: {sub} '
      '\nMultiplicação: {mult}'
      '\nDivisão: {div}'
      '\nResto: {resto}'.format(soma=soma, mult=mult, resto=resto, div=div, sub=sub,))