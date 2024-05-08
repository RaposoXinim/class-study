import tkinter as tk

janela = tk.Tk()

ola= tk.Label(text="Brincando com Tkinter",
              foreground="#E6E6FA", #fg=....
              backgroun="#FF1493", #bg=......
              width=40,
              height=40
              )
botao = tk.Button(
    text="Botão",
    width=25,
    height=5,
    bg= "blue",
    fg="yellow"
)
entry=tk.Entry(fg="yellow", bg="blue", width=50)

ola.pack()
botao.pack()
entry.pack()



janela.mainloop()