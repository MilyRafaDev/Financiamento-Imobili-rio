from tkinter import *
from tkinter import ttk

import tkinter as ttk

###Cores###
Branco = '#F2F2F2'
Vermelho = '#D93B75'
Azul = '#8BBBD9'
###########

# Inicio da Interface
janela = Tk()
janela.title('Financiamento Imobiliário')
janela.geometry('500x340')
janela.config(bg=Branco)

#Frame Titulo
titulo = Frame(janela, width=500, height=80, bg=Branco)
titulo.grid(row=0, column=0)
        #Titulo
nome = Label(titulo,text='FINANCIAMENTO IMOBILIÁRIO', font=('Times New Roman',25),fg=Vermelho,bg=Branco, justify='center', anchor=CENTER)
nome.place(x=3, y=10) 
        #Linha
linha = Label(titulo, width=500, height=0, bg=Vermelho)
linha.place(x=0, y=60)
#Final Titulo

#frame interface
interface = Frame(janela, width=500, height=200, bg=Branco)
interface.grid(row=1, column=0)
        #solicitar variavel n
nomelabel = ttk.Label(interface, text='Digite seu nome', font=('Times New Roman', 12), fg=Vermelho)
nomelabel.grid(row=1, column=0, padx=5, pady=5)

nome = ttk.Entry(interface, width=35)
nome.grid(row=1, column=2, padx=5, pady=5)

 #solicitar variavel s
salariolabel = ttk.Label(interface, text='Digite sua renda mensal', font=('Times New Roman', 12), fg=Vermelho)
salariolabel.grid(row=2, column=0, padx=5, pady=5)

salario = ttk.Entry(interface, width=35)
salario.grid(row=2, column=2, padx=5, pady=5)

 #solicitar variavel v
valorlabel = ttk.Label(interface, text='Digite o valor de financiamento', font=('Times New Roman', 12), fg=Vermelho)
valorlabel.grid(row=3, column=0, padx=5, pady=5)

valor = ttk.Entry(interface, width=35)
valor.grid(row=3, column=2, padx=5, pady=5)

 #solicitar variavel a
anoslabel = ttk.Label(interface, text='Digite quantos anos serão de financiamento', font=('Times New Roman', 12), fg=Vermelho)
anoslabel.grid(row=4, column=0, padx=5, pady=5)

anos = ttk.Entry(interface, width=35)
anos.grid(row=4, column=2, padx=5, pady=5)

#frame resultados
resultados = ttk.Frame(janela, width=500, height=120, bg=Azul)
resultados.grid(row=2, column=0)

#encerramento da interface
janela.mainloop()
