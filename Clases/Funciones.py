#Lo primero de todo es importar las librerias necesarias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Nos disponemos a leer el archivo csv
df = pd.read_csv('USA_Housing.csv', sep = ',')
print("El dataset inicial es el siguiente :")
print(df, "\n")

#Como los nombres de las columnas estan en ingles, vamos a traducirlos a español para poder hacer un mejor analisis
#Las columnas iniciales del csv son:
print('-------------Columnas del CSV-----------')
print(df.columns, "\n")
#Ahora lo cambiamos
print("Realizamos el cambio de ingles a español:")
cambioingesp =  {'Avg. Area Income': 'Ganancia Media','Avg. Area House Age':'Edad Casa Media', 'Avg. Area Number of Rooms':'Num Habitaciones Medio', 'Avg. Area Number of Bedrooms': 'Num HabitCama Medio', 'Area Population': 'Poblacion en Area', 'Price':'Precio', 'Address':'Direccion'}
df2 = traduccion(f, traducido)
print("\n")

#Los datos del archivo segun las filas son:
print('------------Datos del CSV-------------')
print('Primeras filas')
print(df.head(), "\n")
print('Últimas filas')
print(df.tail(), "\n")

#Una vez que tenemos los datos, procedemos a explicar sus caracteristicas
print('----------Descripción del CSV----------------')
print("Nos disponemos a explicar los datos anteriores:")
print(df2.describe(), "\n")
print("En estos datos podemos destacar dos cosas:", "\n", "En primer lugar, la media total esta casi en la mitad, coincidiendo con el percentil 50. Esto significa que ambos son el mismo valor.", "\n", "Segundo, como punto minimo y punto maximo, destacamos el numero de habitaciones, la antiguedad y la ganancia generada.")
print('Información datos')
print(df2.info(), "\n")

#Clasificamos los resultados obtenidos anteriormente
print('----------Clasificación de los resultados anteriores --------------')
print('La categoria de los resultados es la siguiente:')
print('Las categorias numericas nombradas anteriormente son: precio, media-salario, media-antig-casa, media-numero-habitaciones,media-numero-dormitorios-casas, poblacion')
