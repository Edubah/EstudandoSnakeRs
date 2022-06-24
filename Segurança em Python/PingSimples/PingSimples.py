import os #Importando a biblioteca "OS" (Integra e os programas e recursos da biblioteca)

print('#' * 60) # Imprimindo o # 60 vezes

ip_ou_host = input('Digite o ip ou host a ser verificado: ') #Criando a variável que solicita o Ping ou o Host

print('-' * 60) #Imprimindo o traço 60 vezes

os.system('ping -n 6 {}'.format(ip_ou_host)) #Chamando o método SYSTEM da biblioteca "OS"

print('-' * 60) #Imprimindo o traço 60 vezes