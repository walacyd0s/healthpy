import tkinter.messagebox
from tkinter import *


def calcular_peso():
    altura = entrada1.get()
    if altura.isalpha():
        tkinter.messagebox.showinfo('Erro', 'Informe valores númericos!')
    else:
        altura = float(entrada1.get())
    peso = entrada2.get()
    if peso.isalpha():
        tkinter.messagebox.showinfo('Erro', 'Informe valores númericos!')
    else:
        peso = float(entrada2.get())
    peso_ideal = peso / (altura * altura)
    imc['text'] = f'IMC: {peso_ideal:.1f}  |'
    if peso_ideal < 16:
        resultado['text'] = 'Magreza Grau III'
    elif (peso_ideal >= 16) and (peso_ideal <= 16.9):
        resultado['text'] = 'Magreza Grau II'
    elif (peso_ideal >= 17) and (peso_ideal <= 18):
        resultado['text'] = 'Magreza Grau I'
    elif (peso_ideal >= 18.5) and (peso_ideal <= 24.9):
        resultado['text'] = 'Peso Adequado'
    elif (peso_ideal >= 25) and (peso_ideal <= 29.9):
        resultado['text'] = 'Pré-Obeso'
    elif (peso_ideal >= 30) and (peso_ideal <= 34.9):
        resultado['text'] = 'Obesidade Grau I'
    elif (peso_ideal >= 35) and (peso_ideal <= 39.9):
        resultado['text'] = 'Obesidade Grau II'
    elif peso_ideal >= 40:
        resultado['text'] = 'Obesidade Grau III'


root = Tk()
root.geometry('240x160+1200+300')
root.configure(background='#F0F8FF')
root.title('HealthPy')

titulo = Label(root, text='Calcule seu peso ideal')
titulo.configure(background='#5F9EA0', font=('Calibri', 14))
titulo.place(x=5, y=20)

label1 = Label(root, text='Altura')
label1.configure(background='#F0F8FF')
label1.place(x=5, y=55)

entrada1 = Entry(root)
entrada1.configure(width=5)
entrada1.place(x=7, y=85)

label2 = Label(root, text='Peso')
label2.configure(background='#F0F8FF')
label2.place(x=60, y=55)

entrada2 = Entry(root)
entrada2.configure(width=5)
entrada2.place(x=62, y=85)

botao = Button(root, text='Calcular', command=calcular_peso)
botao.configure(width=8, height=2, font=('Arial Black', 8))
botao.place(x=105, y=60)

imc = Label(root)
imc.configure(background='#F0F8FF', font=('Arial Black', 8))
imc.place(x=5, y=125)

resultado = Label(root)
resultado.configure(background='#F0F8FF', font=('Arial Black', 8))
resultado.place(x=80, y=125)

root.resizable(False, False)
root.mainloop()
