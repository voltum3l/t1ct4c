from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import random
from pygame import mixer
import sys
from tkinter import simpledialog


def CambiarNombre(num):
	global NamePlayer1
	global NamePlayer2

	if num==1:
		answer = simpledialog.askstring("Jugador 1", "Ingrese el nombre del jugador 1")
		if answer != "":		
			NamePlayer1.set(answer)
		else:
			NamePlayer1.set("Player 1")
	else:
		answer = simpledialog.askstring("Jugador 2", "Ingrese el nombre del jugador 2")
		if answer != "":		
			NamePlayer2.set(answer)
		else:
			NamePlayer2.set("Player 2")

def About():
	messagebox.showinfo("Informacion del Autor",
		"Nombre: E. Gastón Rayes\nGithub: github.com/voltum3l/")

def Cambiar(num):
	global botones
	global i1
	global i2
	global turno
	global contador
	global sound

	sound.play()
	if contador[num] == 0:
		if turno==1:
			botones[num].configure(image=i1)
			turno=2
		else:
			botones[num].configure(image=i2)
			turno=1
		contador[num] = turno
		Calcular(num)
		ActualizarImagenTurno()
	else:
		messagebox.showinfo("ERROR","Casilla Ocupada")

def ActualizarImagenTurno():
	global labelTurno
	labelTurno.config(image=TurnoImagen())

def Calcular(num):
	global proximoturno
	proximoturno=proximoturno + 1
	if HayGanador(num) == False:
		if proximoturno == 9:
			Empate()
			NuevoJuego(1)
	else:
		NuevoJuego(1)

def NuevoJuego(opcion):
	#opcion 1 sigue el mismo juego, opcion 2 se vuelve todo a 0
	global turno
	turno = random.randint(1,2)
	global proximoturno
	proximoturno=0
	global contador
	for i in range(len(contador)):
		contador[i]=0

	global botones
	global i3
	for i in range(len(botones)):
		botones[i].configure(image=i3)
	global puntacionGlobal
	global ScorePlayer1
	global ScorePlayer2
	if opcion==2:
		ScorePlayer1=0
		ScorePlayer2=0

	puntacionGlobal[0].configure(text=ScorePlayer1)
	puntacionGlobal[1].configure(text=ScorePlayer2)
	ActualizarImagenTurno

def HayGanador(num):
	global contador
	global ScorePlayer1
	global ScorePlayer2
	global turno
	global NamePlayer1
	global NamePlayer2

	ganador=False

	if contador[0] == contador[1] == contador [2] and contador[0] != 0:
		ganador = True
	elif contador[0] == contador[4] == contador [8] and contador[0] != 0:
		ganador = True
	elif contador[0] == contador[3] == contador [6] and contador[0] != 0:
		ganador = True
	elif contador[1] == contador[4] == contador [7] and contador[1] != 0:
		ganador = True
	elif contador[2] == contador[4] == contador [6] and contador[2] != 0:
		ganador = True
	elif contador[2] == contador[5] == contador [8] and contador[2] != 0:
		ganador = True
	elif contador[3] == contador[4] == contador [5] and contador[3] != 0:
		ganador = True
	elif contador[6] == contador[7] == contador [8] and contador[6] != 0:
		ganador = True
	else:
		ganador = False

	var1=int(ScorePlayer1)
	var2=int(ScorePlayer2)

	if ganador:
		if turno==1:
			var1=var1+1
			messagebox.showinfo("GANADOR","Ha ganado "+NamePlayer1.get())
			ScorePlayer1=var1
		else:
			var2=var2+1
			messagebox.showinfo("GANADOR","Ha ganado "+NamePlayer2.get())
			ScorePlayer2=var2
	return ganador

def Empate():
	messagebox.showinfo("Resultado","Empate")

def TurnoImagen():
	global turno
	global i1
	global i2
	if turno == 1:
		return i1
	else:
		return i2

def Exit():
	option=messagebox.askquestion("Salir","¿Cerrar el programa?")
	if option=="yes":
		sys.exit()
def CambiarJugadores():
	pass
###########################################################################
###########################################################################
###########################################################################

mixer.init() 
sound=mixer.Sound("pop.wav")

turno=random.randint(1,2)
proximoturno=0
contador={}
for i in range(9):
	contador[i]=0

root = Tk()
root.title("Ta Te Ti")


barraMenu=Menu(root)

root.config(menu=barraMenu,bg="black")
root.resizable(0,0)
root.geometry("400x450")

fileMenu=Menu(barraMenu,tearoff=0)
fileMenu.add_command(label="Nuevo Juego",command=lambda:NuevoJuego(2))
fileMenu.add_separator()
fileMenu.add_command(label="Cambiar Jugador 1",command=lambda:CambiarNombre(1))
fileMenu.add_command(label="Cambiar Jugador 2",command=lambda:CambiarNombre(2))
fileMenu.add_separator()
fileMenu.add_command(label="Exit",command=Exit)

acercaDe=Menu(barraMenu,tearoff=0)
acercaDe.add_command(label="Desarrollador",command=About)

barraMenu.add_cascade(label="Opciones",menu=fileMenu)
barraMenu.add_cascade(label="Informacion",menu=acercaDe)


image1=Image.open('C:/Users/BATMAN/Desktop/TicTac/cruz.png')
image1=image1.resize((25,25 ), Image.ANTIALIAS)
image2=Image.open('C:/Users/BATMAN/Desktop/TicTac/circulo.png')
image2=image2.resize((25,25 ), Image.ANTIALIAS)
image3=Image.open('C:/Users/BATMAN/Desktop/TicTac/empty.png')
image3=image3.resize((25,25), Image.ANTIALIAS)
i1 = ImageTk.PhotoImage(image1)
i2 = ImageTk.PhotoImage(image2)
i3 = ImageTk.PhotoImage(image3)


frame0=Frame(root)
#frame0.config(bg="black")
frame0.grid(row=0,column=0,sticky="n",pady=5)
labelTurno=Label(frame0,text="TURNO",width=15,height=3)
labelTurno.grid(row=0,column=0,pady=8,padx=15,sticky="nsew")
imagenTurno=TurnoImagen()
labelTurno=Label(frame0,image=imagenTurno)
labelTurno.grid(row=0,column=1,pady=8,padx=15,sticky="nsew")

frame1=Frame()
frame1.config(width="400",height="50")


ScorePlayer1=StringVar()
ScorePlayer2=StringVar()

ScorePlayer1="0"
ScorePlayer2="0"

NamePlayer1=StringVar()
NamePlayer2=StringVar()
NamePlayer1.set("Player 1")
NamePlayer2.set("Player 2")

puntuacion1=Label(frame1,text="Score",fg="black")
puntuacion1.grid(row=0,column=0,padx=2,pady=1)
puntuacion1Dyn=Label(frame1,text=ScorePlayer1,fg="black")
puntuacion1Dyn.grid(row=1,column=0,padx=2,pady=1)
name1=Label(frame1,textvariable=NamePlayer1,bg="red",fg="white")
name1.grid(row=0,column=1,padx=2,pady=1)
puntuacion2=Label(frame1,text="Score",fg="black")
puntuacion2.grid(row=0,column=3,padx=2,pady=1)
puntuacion2Dyn=Label(frame1,text=ScorePlayer2,fg="black")
puntuacion2Dyn.grid(row=1,column=3,padx=2,pady=1)
name2=Label(frame1,textvariable=NamePlayer2,bg="blue",fg="white")
name2.grid(row=0,column=2,padx=2,pady=1)

img1=Label(frame1,image=i1)
img2=Label(frame1,image=i2)
img1.grid(row=1,column=2,pady=1)
img2.grid(row=1,column=1,pady=1)

frame1.grid(row=1,column=0)

puntacionGlobal=[puntuacion1Dyn,puntuacion2Dyn]

frame2=Frame()
frame2.config(width=400,height=10,bg="black")
frame2.grid(row=2,column=0)


frame3=Frame()
frame3.config(bg="black")
frame3.grid(row=3,column=0)
ancho=120
alto=95

boton0=Button(frame3,image=i3,width=ancho,height=alto)
boton0.grid(row=0,column=0,padx=1)
boton1=Button(frame3,image=i3,width=ancho,height=alto)
boton1.grid(row=0,column=1,padx=1)
boton2=Button(frame3,image=i3,width=ancho,height=alto)
boton2.grid(row=0,column=2,padx=1)
boton3=Button(frame3,image=i3,width=ancho,height=alto)
boton3.grid(row=1,column=0,padx=1)
boton4=Button(frame3,image=i3,width=ancho,height=alto)
boton4.grid(row=1,column=1,padx=1)
boton5=Button(frame3,image=i3,width=ancho,height=alto)
boton5.grid(row=1,column=2,padx=1)
boton6=Button(frame3,image=i3,width=ancho,height=alto)
boton6.grid(row=2,column=0,padx=1)
boton7=Button(frame3,image=i3,width=ancho,height=alto)
boton7.grid(row=2,column=1,padx=1)
boton8=Button(frame3,image=i3,width=ancho,height=alto)
boton8.grid(row=2,column=2,padx=1)

botones=[boton0,boton1,boton2,boton3,boton4,boton5,boton6,boton7,boton8]

boton0.config(command=lambda:Cambiar(0))
boton1.config(command=lambda:Cambiar(1))
boton2.config(command=lambda:Cambiar(2))
boton3.config(command=lambda:Cambiar(3))
boton4.config(command=lambda:Cambiar(4))
boton5.config(command=lambda:Cambiar(5))
boton6.config(command=lambda:Cambiar(6))
boton7.config(command=lambda:Cambiar(7))
boton8.config(command=lambda:Cambiar(8))

root.mainloop()
