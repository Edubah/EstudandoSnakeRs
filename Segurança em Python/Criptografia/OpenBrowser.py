import webbrowser
from tkinter import * #Significa importar tudo

root = Tk( ) #Quando há um espaço nos parênteses significa none

root.title('Abrir o Browser') #Título da Interface
root.geometry('300x200') #Tamanho da interface

def google(): #Função para abrir o web browser no goolge
    webbrowser.open(('www.goolge.com'))


mygoogle= Button(root, text='Abrir o Google', command=google).pack(pady=28)
#mygoolge recebe um botão.

root.mainloop()