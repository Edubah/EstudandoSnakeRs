import hashlib

string = input('Digite o texto a ser gerado a hash: ')

#resultados = hashlib.md5(b'Python Security') #O "b" antes dos apóstrofos são usadas para converter o que há dentro dos apóstrofos em BYTES


menu = int(input('''   #### MENU - ESCOLHA O TIPO DE HASH ####
                1) - MD5'
                2) - SHA1'
                3) - SHA256'
                4) - SHA512'
                Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultados = hashlib.md5((string.encode('utf-8')))
    print("A hash MD5 da string: ",string, 'é: ', resultados.hexdigest())
elif menu == 2:
    resultados = hashlib.sha1((string.encode('utf-8')))
    print("A hash SHA1 da string: ", string, 'é: ', resultados.hexdigest())
elif menu == 3:
    resultados = hashlib.sha256((string.encode('utf-8')))
    print("A hash SHA256 da string: ", string, 'é: ', resultados.hexdigest())
elif menu == 4:
    resultados = hashlib.sha512((string.encode('utf-8')))
    print("A hash SHA512 da string: ", string, 'é: ', resultados.hexdigest())

else:
    print('Algo de errado aconteceu, por favor tente novamente!')