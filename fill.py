import tkinter as tk
janela = tk.Tk()
frame1= tk.Frame(master=janela,height=100, bg="red")
frame1.pack(fill=tk.X)
frame2= tk.Frame(master=janela,height=50, bg="green")
frame2.pack(fill=tk.X)
frame3= tk.Frame(master=janela,height=25, bg="blue")
frame3.pack(fill=tk.X)
janela.mainloop()

