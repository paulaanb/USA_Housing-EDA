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
