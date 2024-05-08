import tkinter as tk

def ao_focar(event):
    if entrada.get() == "Digite o seu nome aqui!":
        entrada.delete(0, "end")
        entrada.config(fg="black") #altera o cor de texto para preto

def ao_desfocar(event):
    if not entrada.get():
        entrada.insert(0, "Digite seu nome aqui!")
        entrada.config(fg="gray") # Altera a cor do texto de volta para cinza

janela= tk.Tk()
entrada = tk.Entry(width=40, bg="white", fg="gray")
entrada.pack()
entrada.insert(0, "Digite o seu nome aqui!")

#quando a caixa de entrada ganha foco
entrada.bind("<FocusIn>", ao_focar)

#quando a caixa de entrada perde o foco
entrada.bind("<FocusOut>", ao_desfocar)

janela.mainloop()