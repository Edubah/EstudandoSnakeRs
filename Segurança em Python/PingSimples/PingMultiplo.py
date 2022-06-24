import os, time #Bibliotecas importadas

with open('host.txt') as file: #"Com" a "abertura" do arquivo 'host.txt' "como" um "arquivo"
    dump = file.read() #Faz a variável "dump" ler o arquivo como o .READ()
    dump = dump.splitlines() #Colocando o dump em linhas separads


    for ip in dump: #Para cada IP no DUMP
        print('Verificando o IP', ip) #Imprime
        print('-' * 60)
        os.system('ping -n 2 {}'.format(ip)) #Faz a verificação por ip
        print('-' * 60)
        time.sleep(3)