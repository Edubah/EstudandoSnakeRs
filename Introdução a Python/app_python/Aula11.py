

lista = [1, 10]
try:
    div = 10 / 0
    numero = lista[1]
    x = a
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
except ZeroDivisionError:
    print('não é possível realizar uma divisão por zero!')
except IndexError:
    print('Erro ao acessar um índice da lista!')

#else: Ele irá ser executado quando não houver mais exeções!
#Finally executa o programa mesmo com excessões

