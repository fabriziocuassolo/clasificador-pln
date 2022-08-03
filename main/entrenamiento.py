#Realizamos las importaciones necesarias:
import nltk
import regex as re
import operator
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import collections
import clasificador as clas

path_ciencia = 'C:\\Users\\fabri\\Clasificador_PLN\\main\\train_ciencia\\'
path_politica = 'C:\\Users\\fabri\\Clasificador_PLN\\main\\train_politica\\'
path_economia = 'C:\\Users\\fabri\\Clasificador_PLN\\main\\train_economia\\'
path_deportes = 'C:\\Users\\fabri\\Clasificador_PLN\\main\\train_deportes\\'

def entrenamiento_politica(file):

    filtradas =  clas.pre_procesado(file)
    train_politica = open(f'{path_politica}train_politica.txt','a',errors='ignore')

    for v in filtradas:

        train_politica.write(v+"\n")

    train_politica.close()

    return train_politica


def entrenamiento_economia(file):

    filtradas =  clas.pre_procesado(file)
    train_economia = open(f'{path_economia}train_economia.txt','a',errors='ignore')

    for v in filtradas:

        train_economia.write(v+"\n")

    train_economia.close()
    return train_economia


def entrenamiento_deportes(file):

    filtradas =  clas.pre_procesado(file)
    train_deportes = open(f'{path_deportes}train_deportes.txt','a',errors='ignore')

    for v in filtradas:

        train_deportes.write(v+"\n")

    train_deportes.close()
    return train_deportes


def entrenamiento_ciencia(file):
    
    filtradas =  clas.pre_procesado(file)

    train_ciencia = open(f'{path_ciencia}train_ciencia.txt','a',errors='ignore')

    for v in filtradas:

        train_ciencia.write(v+"\n")

    train_ciencia.close()
    return train_ciencia
    


def modelizador(arch):

    #Creamos el diccionario de entrenamiento de cada categoria (en una lista) a partir del archivo que se genero.
    train = open(arch, 'r')
    dic = train.read().split('\n')
    train.close()
    #Una vez que tengo el diccionario de entrenamiento ya creado me fijo cuales son las mas repetidas dentro del mismo. El restultado que me da voy a tener en cuenta un umbral x cantidad de repetidas.
    #Si supera el umbral es mayor o igual a 5 las considero validas para mi clasificador final de categoria
    clasificador = [x for x, y in collections.Counter(dic).items() if y >= 5]
    return clasificador
    

    
    



