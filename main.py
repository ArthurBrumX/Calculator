# Importando tkinter
from tkinter import * 
from tkinter import ttk

#cores

cor1 = "#95bcbd"

janela = Tk()
janela.title("Calculadora")
janela.geometry("235x318")

frame_tela = Frame(janela, width = 235, height=50, bg = cor1)
frame_tela.grid(row=0, column=0)

janela.mainloop()