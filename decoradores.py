''' 
# EJEMPLO DECORADOR QUE TRANSFORMA A MINUSCULA EL MENSAJE Y EL NOMBRE
def mayusculas(func):
    def wrapper(texto):
        return func(texto).upper()
    return wrapper

@mayusculas
def mensaje(nombre):
    return "{} recibiste un mensaje".format(nombre)

print(mensaje('Carlos')) 


# EJEMPLO DECORADOR QUE TRANSFORMA A MAYUSCULA EL MENSAJE Y EL NOMBRE
def minusculas(func):
    def wrapper(texto):
        print("Se cambió lo siguiente a minúscula: ")
        return func(texto).lower()
    return wrapper

@minusculas
def mensaje(nombre):
    return "{} HAS RECIBIDO UN MENSAJE".format(nombre)

print(mensaje('CARLOS'))
'''

import json
import pandas as pd
from urllib.request import urlopen

# carga del dataframe con la data de la plataforma localbitcoins
url = ("https://jsonplaceholder.typicode.com/comments")
data = json.load(urlopen(url))
df = pd.DataFrame(data=data)

# Decorator function that return the null values of a dataset
def null_values(func):
    def wrapper(df):
        return print(func(df.isnull().sum()))
    return wrapper

@null_values
def shape_of_df(df):
    return df.shape

print(shape_of_df(df))