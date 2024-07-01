import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Atividade do botão de clique")
root.geometry("200x200")
cliques = 0
message1 = tk.Label(root, text="Aperte no botão!")
message1.pack()

def callback():
    global cliques
    cliques += 1
    message1.config(text=f"Número de cliques: {cliques}")
    print("O botão apertar foi apertado!")
    # do something

def apaga():
    global cliques
    cliques = 0
    message1.config(text=f"Número de cliques: {cliques}")
    print("O botão apagar foi apertado!")
    # do something


botao= ttk.Button(
   root, 
   text="Little button",
   command=callback
)

botao2= ttk.Button(
   root,
   text="Apaga",
   command=apaga
)
botao.pack()
botao2.pack()
root.mainloop()