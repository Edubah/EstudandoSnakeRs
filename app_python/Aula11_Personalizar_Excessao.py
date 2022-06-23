class Erro(Exception): #Classe que está herdando de Excessão!
    pass #Apenas para que não dê erro, utiliza o passa para "PASSAR"

class InputError(Erro): #É obrigatório ter uma classe de erro herdando de EXCESSÃO para que você crie uma classe ERROR
    def __init__(self, message):
        self.message = message
while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)

        if x > 10:
            raise InputError('Nota não pode ser maior que 10') #Comando para forçar uma excessão!
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0@$♦')
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números!')
    except InputError as ex:
        print(ex)