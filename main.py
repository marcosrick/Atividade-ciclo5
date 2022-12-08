import sqlite3
import tkinter
from tkinter import *

def calculoIMC():

     con = sqlite3.connect("bdcalculadoraimc.db")
     cur = con.cursor()
     cur.execute("CREATE TABLE IF NOT EXISTS dados(nome TEXT, endereco TEXT, altura INTEGER,peso INTEGER)")
     cur.execute("INSERT INTO dados(nome, endereco, altura, peso) VALUES (?,?,?,?)",
                 (nomeusuario.get(), enderecousuario.get(), recebealtura.get(), recebepeso.get()))
     con.commit()

     recebePeso = float(recebepeso.get())
     recebeAltura = float(recebealtura.get())

     metroAltura = recebeAltura / 100

     imcrecebe = recebePeso / (metroAltura * metroAltura)

     if imcrecebe < 17:
         resultadorecebe["text"] = f'Bem abaixo do peso ideal\nO seu IMC total é {imcrecebe:.2f}'
     elif imcrecebe >= 17 and imcrecebe <= 18.49:
         resultadorecebe["text"] = f'Abaixo do peso ideal\nO seu IMC total é {imcrecebe:.2f}'
     elif imcrecebe >= 18.50 and imcrecebe <= 24.99:
         resultadorecebe["text"] = f'Peso ideal\nO seu IMC total é {imcrecebe:.2f}'
     elif imcrecebe >= 25 and imcrecebe <= 29.99:
         resultadorecebe["text"] = f'Acima do peso ideal\nO seu IMC total é {imcrecebe:.2f}'
     elif imcrecebe >= 30 and imcrecebe <= 34.99:
         resultadorecebe["text"] = f'Obesidade grau I\nO seu IMC total é {imcrecebe:.2f}'
     elif imcrecebe >= 35 and imcrecebe <= 39.99:
         resultadorecebe["text"] = f'Obesidade grau II\nO seu IMC total é {imcrecebe:.2f}'
     else:
         resultadorecebe["text"] = f'Obesidade grau III\nO seu IMC total é {imcrecebe:.2f}'

def reset():

     reiniciar = ''
     resultadorecebe["text"] = reiniciar

     nomeusuario.delete(0, END)
     enderecousuario.delete(0, END)
     recebealtura.delete(0, END)
     recebepeso.delete(0, END)

calculadoraimc=Tk()
calculadoraimc.title("Cálculadora IMC - Índice de Massa Corporal")
calculadoraimc.geometry("500x250")
calculadoraimc.configure(background="#000000")

Label(calculadoraimc,text="Nome do Paciente: ",background="black",foreground="white",anchor=W).place(x=10,y=27,width=200,height=23)
nomeusuario=Entry(calculadoraimc)
nomeusuario.place(x=160, y=30, width=327, height=25)

Label(calculadoraimc,text="Endereço Completo: ",background="black",foreground="white",anchor=W).place(x=10,y=62,width=200,height=23)
enderecousuario=Entry(calculadoraimc)
enderecousuario.place(x=160, y=65, width=327, height=25)

Label(calculadoraimc,text="Altura (cm) ",background="black",foreground="white",anchor=W).place(x=10,y=97,width=100,height=23)
recebealtura=Entry(calculadoraimc)
recebealtura.place(x=160, y=100, width=127, height=25)

Label(calculadoraimc,text="Peso (Kg) ",background="black",foreground="white",anchor=W).place(x=10,y=132,width=100,height=23)
recebepeso=Entry(calculadoraimc)
recebepeso.place(x=160, y=135, width=127, height=25)

resultadorecebe = Label(calculadoraimc, text="", background="white", foreground="#000000", font="#000000")
resultadorecebe.place(x=297, y=100, width=190, height=90)

Button(calculadoraimc,text="Calcular",command=calculoIMC).place(x=60,y=203,width=100,height=21)
Button(calculadoraimc,text="Reiniciar",command=reset).place(x=160,y=203,width=100,height=21)
Button(calculadoraimc,text="Sair",command=calculadoraimc.quit).place(x=345,y=203,width=100,height=21)

calculadoraimc.mainloop()
