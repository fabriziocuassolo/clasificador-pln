#Realizamos las importaciones necesarias:
import nltk
import regex as re
import operator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import collections
from entrenamiento import *


#Definimos nuestra funcion clasificadora:

path_ciencia = 'C:\\Users\\fabri\\Clasificador_PLN\\main\\train_ciencia\\'
path_politica = 'C:\\Users\\fabri\\Clasificador_PLN\\main\\train_politica\\'
path_economia = 'C:\\Users\\fabri\\Clasificador_PLN\\main\\train_economia\\'
path_deportes = 'C:\\Users\\fabri\\Clasificador_PLN\\main\\train_deportes\\'

def pre_procesado(file):

    # Importamos el archivo a procesar
    archivo = open(file,'r',encoding = 'UTF-8',errors='ignore')
    corpus = archivo.read()
    archivo.close()
    TextoPreProc = corpus

    #Quito los saltos de linea
    TextoPreProc = re.sub(r'\n',' ', TextoPreProc)

    #Quito los espacios extra
    TextoPreProc = re.sub(r'\.\s\s',". ", TextoPreProc)
    TextoPreProc = re.sub(r'\s\s'," ",TextoPreProc)

    #Quitamos caracteres especiales
    TextoPreProc = re.sub(r'[^\w\s]',"", TextoPreProc)

    #Quitamos numeros
    TextoPreProc = re.sub(r'[0-9]+', '', TextoPreProc)  

    #Tokenizamos por palabras.
    tokens = nltk.word_tokenize(TextoPreProc)

    #Ponemos en minusculas todo los tokens para normalizar.
    minusculas = {w.lower() for w in tokens}

    #Creamos la lista de stopwords y lo convertimos en set para poder filtrarlo
    f = open('stop_words.txt', 'r', encoding='utf8')
    stopwords1 = f.read().split('\n')
    f.close()
    stopwords1 = set(stopwords1)

    #Creamos una lista en donde vamos a guardar todas las palabras filtradas
    palabras_filtradas = []

    #Guardamos finalmente las palabras filtradas.
    for i in minusculas:
        if i not in stopwords1:
            palabras_filtradas.append(i)

    return palabras_filtradas
        

def clasificador(palabras_filtradas):

    dic_politica = modelizador(f'{path_politica}train_politica.txt')
    dic_economia = modelizador(f'{path_economia}train_economia.txt')
    dic_deportes = modelizador(f'{path_deportes}train_deportes.txt')
    dic_ciencia = modelizador(f'{path_ciencia}train_ciencia.txt')

    #Creo contadores para cada categoria, el que mas matches tenga sera la prediccion final para nuestro modelo clasificador de categorias.


    poli=0
    econo=0
    deporte=0
    cienci=0

    categoria_ganadora = {}


    for p in palabras_filtradas:
            
        for pol in dic_politica:
                
            if p == pol:
                poli = poli + 1
                categoria_ganadora.update({'POLITICA':poli})
            
        for eco in dic_economia:
                
            if p == eco:
                econo = econo + 1
                categoria_ganadora.update({'ECONOMIA':econo})
                    
        for dep in dic_deportes:
                
            if p == dep:
                deporte = deporte + 1
                categoria_ganadora.update({'DEPORTES':deporte})
            
        for cie in dic_ciencia:
                
            if p == cie:
                cienci = cienci + 1
                categoria_ganadora.update({'CIENCIA':cienci})
                    

    #Devolvemos el resultado final de nuestra prediccion

    ganador = max(categoria_ganadora.items(), key= operator.itemgetter(1))[0]
    return ganador




