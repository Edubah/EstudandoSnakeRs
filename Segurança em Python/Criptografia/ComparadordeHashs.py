import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160') #Hash1 vai receber da HASHLIB um construtor chamado new, dentro dos () diz qual algoritmo ele utilizará

hash1.update(open(arquivo1, 'rb').read()) #Aqui diz qual arquivo ele vai abrir para comparar o hash

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest(): #Digest é o resumo passado pelos updates
    print(f'O arquivo: {arquivo1} é diferente do arquivo: {arquivo2}.')
    print(f'O hash do arquivo A.txt é: ', hash1.hexdigest())
    print(f'O hash do arquivo B.txt é: ', hash2.hexdigest())
else:
    print(f'O arquivo {arquivo1} é igual ao arquivo: {arquivo2}.')
    print(f'O hash do arquivo A.txt é: ', hash1.hexdigest())
    print(f'O hash do arquivo B.txt é: ', hash2.hexdigest())