import tkinter as tk

def clicado():
    label.config(text="Botão Clicado!")

janela = tk.Tk()
janela.title("Exemplo Tkinter")

label= tk.Label(janela, text="Olá, Tkinter!")
label.pack()

botao = tk.Button(janela, text="Clique em Mim", command=clicado)
botao.pack()
janela.mainloop()