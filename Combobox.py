import tkinter as tk
from tkinter import ttk

def selecionar_mes(event):
    selected_month = combo.get()
    print(f"Você selecionou: {selected_month}")

janela = tk.Tk()
janela.geometry('200x100')
labelTop = tk.Label(janela, text="Meses")
labelTop.grid(column=0, row=0)
meses = ["Janeiro", "Fevereiro", "Março", "Abril"]
combo = ttk.Combobox(janela, values=meses)
combo.grid(column=0, row=1)
combo.current(1)
combo.bind("<<ComboboxSelected>>", selecionar_mes)
janela.mainloop()