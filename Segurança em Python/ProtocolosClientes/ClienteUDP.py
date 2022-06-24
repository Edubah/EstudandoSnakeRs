import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Criando o objeto de conexão "S"

print('Cliente socket criado com sucesso!') #Após criado, informa o sucesso

host = 'localhost' #Definiu o host
porta = 5433 #Definiu a porta
mensagem = 'Olá seu Filho da Puta!' #Mensagem que será enviada e recebida

try:
    print('Cliente: ' + mensagem) #Imprime na tela
    s.sendto(mensagem.encode(), (host, 5434)) #Envia a mensagem empacotada para a porta

    dados, sevidor = s.recvfrom(4096) #Dados e Servidor irão receber uma resposta de 4096bytes
    dados = dados.decode() #A variável vai desempacotar a mensagem
    print('Cliente: ' + dados)

finally:
    print('Cliente: Fechando a conexão!') #Imprime na tela
    s.close() #Fecha a conexão para não ficar em loop