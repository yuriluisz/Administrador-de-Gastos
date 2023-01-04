from tkinter import *

def calculocomida():
    gcomida = open("food.txt", "a")
    ginpcomida = inputcomida.get("1.0", END)
    gcomida.write(ginpcomida)
    rcomida = open("food.txt", "r")
    readcomida = rcomida.readlines()
    for i in readcomida:
        somadiaria = i + readcomida
    print(somadiaria)

totaldiario = "Suamae"
totalmensal = "Seupai"


janela = Tk()
janela.title("Pagina principal")

f1 = Frame(janela)
f1.grid(row=0)
f2 = Frame(janela)
f2.grid(column=0, row=1)
f3 = Frame(janela)
f3.grid(column=1, row=1)
f4 = Frame(janela)
f4.grid(column=2, row=1)
f5 = Frame(janela)
f5.grid(column=3, row=1)

label1 = Label(f1, text="Olá, Seja bem-vindo!")
label1.grid(column=0, row=0, padx=5, pady=5)

label2 = Label(f1, text="Informe-nos dos seus gastos diario!")
label2.grid(column=0, row=1)

label3 = Label(f2, text="comida:")
label3.grid(column=0, row=0, padx=5, pady=5)
inputcomida = Text(f2, height=1, width=30)
inputcomida.grid(column=0, row=1, padx=5, pady=5)
totaldiariocomida = Label(f3, text=totaldiario)
totaldiariocomida.grid(column=0, row=0, padx=5, pady=5)
totalmensalcomida = Label(f4, text=totalmensal)
totalmensalcomida.grid(column=0, row=0, padx=5, pady=5)
calccomida = Button(f5, text="Calcular", command=calculocomida)
calccomida.grid(column=0, row=0, padx=5, pady=5)

janela.mainloop()