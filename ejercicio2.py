# Se importa la libreria Tkinter con todas sus funciones
from errno import ENETRESET
from importlib.metadata import entry_points
from tkinter import *
from tkinter import ttk


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
ventana_principal.config(bg="black")


#---------------------
# Frame Entrada
#---------------------

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="ivory2", width=780, height=240)
frame_entrada.place(x=10,y=10)

#Etiqueta para titulo de app
titulo= Label(frame_entrada, text="Colegio San José de Guanentá ")
titulo.config(bg="yellow", fg="blue", font=("Arial", 16))
titulo.place(x=240,y=10)

#Etiqueta para subtitulo de app
subtitulo= Label(frame_entrada, text="Especialidad en Sistemas")
subtitulo.config(bg="yellow", fg="blue", font=("Arial", 12))
subtitulo.place(x=240,y=40)

#Etiqueta para subtitulo 2 de app
subtitulo2= Label(frame_entrada, text="Suma de Dos Enteros")
subtitulo2.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
subtitulo2.place(x=240,y=70)

#Imagen - Logo de la App
logo= PhotoImage(file="goku.png")
etiq_logo=Label(frame_entrada, image=logo)
etiq_logo.config(bg="ivory2")
etiq_logo.place(x=10,y=10)

# etiqueta para valor a
etiq_a=Label(frame_entrada, text="a = ")
etiq_a.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_a.place(x=390, y=120)

#Entry para el valor A
entry_a=Entry(frame_entrada, width=4)
entry_a.config(font=("Arial", 20), justify=CENTER)
entry_a.focus_set()
entry_a.place(x=440,y=120)

# etiqueta para valor b
etiq_b=Label(frame_entrada, text="b = ")
etiq_b.config(bg="ivory2", fg="blue", font=("Arial", 15), anchor=CENTER)
etiq_b.place(x=585, y=120)

#Entry para el valor B
entry_b=Entry(frame_entrada)
entry_b.config(font=("Arial", 20), width=4)
entry_b.place(x=682,y=120)


#---------------------
# Frame Operaciones
#---------------------

frame_operaciones=Frame(ventana_principal)
frame_operaciones.config(bg="cornflower blue", width=780, height=120)
frame_operaciones.place(x=10,y=260)

#Boton para Sumar
# bt_sumar= Button(frame_operaciones, text="Sumar", width=10)
# bt_sumar.place(x=195, y=60)
bt_sum= PhotoImage(file="sumar.png")
bt_sumar= Button(frame_operaciones, image=bt_sum, width=105, height=105)
bt_sumar.place(x=116, y=7)



# bt_borrar=Button(frame_operaciones, text="Borrar", width=10)
# bt_borrar.place(x=390, y=60)
bt_bor= PhotoImage(file="borrar.png")
bt_borrar= Button(frame_operaciones, image=bt_bor, width=105, height=105)
bt_borrar.place(x=337, y=7)





# bt_salir=Button(frame_operaciones, text="Salir", width=10)
# bt_salir.place(x=585, y=60)
bt_sal= PhotoImage(file="cerrar.png")
bt_salir= Button(frame_operaciones, image=bt_sal, width=105, height=105)
bt_salir.place(x=585, y=7)
bt_salir.config(command=quit)
#---------------------
# Frame Resultados
#---------------------

frame_resultados=Frame(ventana_principal)
frame_resultados.config(bg="indian red", width=780, height=100)
frame_resultados.place(x=10,y=390)


resultado=Text(frame_resultados, width=93, height=4)
resultado.place(x=10,y=10)

#Se ejecuta el metodo mainloop de la clase Tk a traves de la instancia ventana_principal.Este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga, por ejemplo, click en boton, escribir en caja de texto, etc.Cada acción del usuario se conoce como un evento.El método mainloop es un bucle infinito

ventana_principal.mainloop()

