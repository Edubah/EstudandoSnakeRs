import shutil   #Biblioteca do python

def escrever_arquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close



def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n') #Split serve para sempre que o split encontrar algo mencionado em seus parâmetros ele fará o item pertencer a uma lista
    #print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo)

def move_arquivos(nome_arquivo):
    shutil.move(nome_arquivo)



#copia_arquivo('notas.txt')
#lista_media = media_notas('notas.txt')
#print(lista_media)
#escrever_arquivo('Primeira linha. \n')
#aluno = 'Brenda, 0, 5, 8, 9 \n'
#atualizar_arquivo('notas.txt', aluno)
#ler_arquivo('teste.txt')