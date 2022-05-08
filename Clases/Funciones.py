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

#Definimos una funcion para comparar
def bar_plt(df, variable):
    variable = df[variable]
    valorvariable = variable.value_counts()
    #Establecemos los valores de la grafica
    plt.figure(figsize=(5, 2)) 
    plt.bar(valorvariable.index, valorvariable) 
    plt.xticks(valorvariable.index, valorvariable.index.values) 
    plt.ylabel('Frecuencia')
    plt.tittle(variable)
    plt.show()
    
    print("{}:\n{}".format(variable, valorvariable))

#Definimos la funcion para calcular la media y la varianza
def media(df, variable):
    media =  (df[variable].sum())/(df[variable].count())
    return media

def varianza(df, variable, media):
    varianza = ((df[variable] - media)**2).sum()/(df[variable].count())
    return varianza

#Representamos en un historiograma los datos
def histograma(df, variable, media, desviaciontipica, varianza, min, max):

    if media < 10:
        a = 0.01
    else:
        a = 1
    x = np.arange(min, max + a, a)
    f = 1/(desviaciontipica * np.sqrt(2*np.pi)) * np.exp(-(x - media) ** 2/(2 * varianza))
    fig, ax1 = plt.subplots()
    ax1.hist(df[variable], bins= 50)
    ax2 = ax1.twinx()
    ax2.plot(x, f, color = 'black', linestyle = 'dashed', linewidth=3)
    plt.title('Histograma de {}'.format(variable))
    plt.axvline(media, color='red', linestyle='dashed', linewidth=1,label = str(media))
    plt.legend(loc='upper right')
    plt.savefig('img/Histograma_de_{}'.format(variable) + '.png', bbox_inches='tight')
    plt.show()


#Representamos las graficas
def graficas(df):
    rango = [0, 2, 4, 6, 8, 10]
    nombres = ['0-2', '2-4', '4-6', '6-8', '8-10']
    
    df['media-antig-casa'] = pd.cut(df['media-antig-casa'], rango, labels = nombres)
    df2 = df.groupby('media-antig-casa').mean()
    df3= df.groupby('media-antig-casa').count()
    df4 = df2[['precio', 'poblacion', 'media-salario']]
    df5 = df2[['media-numero-habitaciones', 'media-numero-dormitorios-casas']]
    df3.rename(columns={'precio': 'numeroVivienda'}, inplace = True)
    plt.subplots()
    plt.xlabel('Número de viviendas por rango de años')
    x = df3['numeroVivienda']
    plt.pie(x, autopct="%0.1f %%", labels=nombres)
    plt.savefig('img/Número_de_viviendas_por_rango_de_años' + '.png', bbox_inches='tight')
    
    df4.plot(kind='bar')
    plt.title('Relación precio/población/salario con la anterior casa')
    plt.savefig('img/Relación_precio_población_salario_con_la_anterior_casa' + '.png', bbox_inches='tight')
    
    df5.plot(kind='bar')
    plt.title('Relación habitaciones y dormitorios con la anterior casa')
    plt.savefig('img/Relación_habitaciones_dormitorios_con_la_anterior_casa' + '.png', bbox_inches='tight')
    
    plt.show()

valornumerico = ['precio', 'media-salario', 'media-antig-casa', 'media-numero-habitaciones','media-numero-dormitorios-casas', 'poblacion']
print('------------Análisis de las variables numéricas del CSV----------------')

for n in valornumerico:
    min = df[n].min()
    max = df[n].max()
    media = round(calculomedia(df, n), 2)
    varianza = round(calculovarianza(df, n, media), 2)
    desviacion_tipica = round((varianza**(1/2)), 2)
    cuartil1 = np.percentile(df[n], 25)
    cuartil2 = np.percentile(df[n], 50)
    cuartil3 = np.percentile(df[n], 75)
    valoresatipicos = criterioDeTukey(df, n, q1, q3)
    print('Los valores atípicos de {}'.format(n) + ' son: ' + str(len(valoresatipicos)) + '\n')
    
    histograma( df, n, media, desviacion_tipica, varianza, min, max)

#Incremento del número de viviendas por año
rango=[1,2,3,4,5,6,7,8,9,10]
nombres= ['3', '4', '5', '6', '7', '8', '9', '10']

df_or['media-antig-casa'] = pd.cut(df_or['media-antig-casa'], rango, labels = nombres)
df_or2 = df_or.groupby('media-antig-casa').mean()
df_or3= df_or.groupby('media-antig-casa').count()
df_or3.rename(columns={'precio': 'numeroViviendas'}, inplace = True)
df_or3['incrementoAnual'] = round(df_or3.numeroViviendas.pct_change() * 100, 2)
df_or3['incrementoAnual'][0]=0
grafica = plt.bar(df_or3.index, df_or3['incrementoAnual'])
print (df_or3['numeroViviendas'],df_or3['incrementoAnual'])
incremento = 0

#Funcion para crear la grafica
for p in grafica:
    width= p.get_width()
    height = p.get_height()
    x, y = p.get_xy()
    plt.text(x + width/2, y + height*1.01, str(df_or3.incrementoAnual[incremento]) + '%', ha = 'center', weight = 'bold')
    incremento = incremento + 1
plt.title('Incremento de viviendas por año')
plt.savefig('img/Incremento_anual' + '.png', bbox_inches='tight')   
plt.show()