import tkinter as tk
janela = tk.Tk()
janela.columnconfigure(0, minsize=250)
janela.rowconfigure([0,1], minsize=100)

label1= tk.Label(text="A")
label1.grid(row=0, column=0, sticky="ne")

label2= tk.Label(text="A")
label2.grid(row=1, column=0, sticky="sw")

janela.mainloop()