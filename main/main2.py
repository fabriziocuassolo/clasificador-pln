#Realizamos las importaciones necesarias:

import os
import nltk
import regex as re
import tkinter
from clasificador import *
from entrenamiento import *
from tkinter import *

#Corro el programa final:

#Establezco los paths en donde estan ubicados todos los txt de cada categoria que voy a usar para entrenar.

path_ciencia = 'C:\\Users\\fabri\\Clasificador_PLN\\main\\train_ciencia\\'
path_politica = 'C:\\Users\\fabri\\Clasificador_PLN\\main\\train_politica\\'
path_economia = 'C:\\Users\\fabri\\Clasificador_PLN\\main\\train_economia\\'
path_deportes = 'C:\\Users\\fabri\\Clasificador_PLN\\main\\train_deportes\\'


#Los guardo en una variable para poder trabajarlos

datos_ciencia = os.listdir(path_ciencia)
datos_politica = os.listdir(path_politica)
datos_economia = os.listdir(path_economia)
datos_deportes = os.listdir(path_deportes)


#Procesamos los textos de cada categoria

for c in datos_ciencia:
    entrenamiento_ciencia(path_ciencia+c)

for p in datos_politica:
    entrenamiento_politica(path_politica+p)

for e in datos_economia:
    entrenamiento_economia(path_economia+e)

for d in datos_deportes:
    entrenamiento_deportes(path_deportes+d)



#Interfaz Grafica
#----------------------------------------------------------------

#Creamos la ventana y le damos su dimension
ventana = Tk()
ventana.title('Clasificador de Noticias')
ventana.geometry('925x400+300+200')
ventana.configure(bg='#171921')
ventana.resizable(False,False)

heading = Label(ventana, text="INGRESE LA NOTICIA A CLASIFICAR",bg='#171921', fg="#00acee", font=('Microsoft Yahei UI Light',18,'bold'))
heading.place(x=245 ,y=5)



entrada = Text(ventana)
entrada.place(x= 160 ,y=60, height=200, width=600)


def resultado():

    with open("entrada.txt", "w",errors='ignore') as text_file:
        texto_input = entrada.get("1.0","end")
        text_file.write(texto_input + '\n')
        text_file.close()
        
    texto_input = pre_procesado("entrada.txt")

    output = clasificador(texto_input)

    output_categoria = Label(ventana, text="Categoria: "+output, bg='#171921', fg="#00acee", font=('Microsoft Yahei UI Light',10,'bold') )
    output_categoria.place(x=365, y = 340)




boton_clasificar = Button(ventana, text="CLASIFICAR", command=resultado, font=('Microsoft Yahei UI Light',10,'bold'))
boton_clasificar.place(x=277,y=285, width = 350)



#ejecución de ventana
ventana.mainloop()






