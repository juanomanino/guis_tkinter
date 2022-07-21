# Se importa la libreria Tkinter con todas sus funciones
from tkinter import *

#---------------------
# Ventana Principal
#---------------------

#Se declara una varaiable que llamamos ventana_principal y que adquiere las caracteristicas de un objeto Tk
ventana_principal=Tk()

#Titulo de la ventana
ventana_principal.title("Juano Niño")

#Establecer tamaño a la pantalla
ventana_principal.geometry("800x300")

#Icono de la ventana principal

#Deshabilitar boton de maximizar
ventana_principal.resizable(0,0)

#Color de fondo de la ventana principal
ventana_principal.config(bg="dark violet")

#Agregamos un widget a la ventana principal
letrero=Label(text="\n\nSistemas, La Mejor!!\n\n", bg="dark violet")
letrero.pack()

#Agregamos un widget a la ventana principal
letrero2=Label(text="\n\nJuano Niño\n\n", bg="dark violet")
letrero2.pack()  

#Agregamos un widget a la ventana principal
letrero3=Label(text="\n\nColegio San José de Guanentá\n\n", bg="dark violet")
letrero3.pack()  

#Se ejecuta el metodo mainloop de la clase Tk a traves de la instancia ventana_principal.Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga, por ejemplo, click en boton, escribir en caja de texto, etc.Cada acción del usuario se conoce como un evento.El método mainloop es un bucle infinito

ventana_principal.mainloop()

