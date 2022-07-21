# Se importa la libreria Tkinter con todas sus funciones
from tkinter import *
import tkinter as tk
import tkinter
from PIL import ImageTk, Image

#---------------------
# Ventana Principal
#---------------------

#Se declara una varaiable que llamamos ventana_principal y que adquiere las caracteristicas de un objeto Tk
ventana_principal=Tk()

#Titulo de la ventana
ventana_principal.title("Juano Niño")

#Establecer tamaño a la pantalla
ventana_principal.geometry("800x500")

#Icono de la ventana principal

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#Color de fondo de la ventana principal
ventana_principal.config(bg="snow")

#---------------------
# Frame Entrada
#---------------------

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="blue4", width=100, height=480)
frame_entrada.place(x=200,y=10)

#---------------------
# Frame Resultados
#---------------------  

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="blue4", width=780, height=100)
frame_resultados.place(x=10,y=210)

#Se ejecuta el metodo mainloop de la clase Tk a traves de la instancia ventana_principal.Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga, por ejemplo, click en boton, escribir en caja de texto, etc.Cada acción del usuario se conoce como un evento.El método mainloop es un bucle infinito

ventana_principal.mainloop()

