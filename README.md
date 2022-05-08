# USA_Housing-EDA
Mi direccion de Github para este repositorio es [https://github.com/paulaanb/USA_Housing-EDA]

En este trabajo hemos hecho un analisis de los datos obtenidos en el CSV dado.

# Explicacion del código
Pasos:

1. Importamos las librerías necesarias:

    -Pandas: esta librería sirve para crear el dataframe y leerlo.
    -Numpy: esta librería sirve para hacer calculos matemáticos como la media o 
    la varianza.
    -Matplotlib: esta libreria sirve para hacer diadramas en dos dimensiones como 
    diagramas de barras.
    
2. Creamos una funcion para que cree el dataframe, lo limpie, lo ordene de menor a mayor,permita leerlo y lo devuelva.

3. Creamos las siguientes funciones estadisticas para proceder al estudio del dataframe:

    -Media: calcula la media con .mean() que es una función de numpy para 
    calcular la media.
    -Desviación típica: calcula la desviación típica con .std() que es una 
    función de numpy para calcular la desviación típica.
    -Varianza: calcula la varianza con .var() que es una función de numpy para 
    calcular la varianza.
    -Mediana: calcula la mediana con .median() que es una función de numpy para 
    calcular la mediana.
    -Moda: calcula la moda con .mode() que es una función de numpy para calcular 
    la moda.
    -Cuartiles: calcula los cuartiles 25 y 75 con .quantile() que es una función 
    de numpy para calcular los cuartiles.
4. Creamos la función menores para responder la pregunta de cuantas naranjas pesan menos de 130

5. Creamos las siguientes gráficas:

    -Diagrama de sectores: utilizamos la librería Matplotlib. Dentro de esta función encontramos uso de diversas funciones como son:

    ax.pie(): se utiliza para trazar gráficos circulares.
    plt.subplots(): es una función que devuelve una tupla que contiene una 
    figura y objeto (s) de ejes. Por lo tanto, al usar fig, ax = plt.subplots() 
    descomprime esta tupla en las variables fig y ax. Teniendo fig es útil si 
    desea cambiar los atributos a nivel de figura o guardar la figura como un 
    archivo de imagen más tarde (por ejemplo, con 
    fig.savefig('yourfilename.png')).
    plt.title(): lo utlizamos para especificar el título de la visualización 
    representada.
    -Diagrma de barras: utilizamos dos librerías: Matplotlib y Seaborn.

    sns.countplot(): se usa para mostrar los conteos de observaciones en cada 
    contenedor categórico usando barras.
    -Diagrama de dispersión: utilizamos la libreía Matplotlib.

    plt.scatter(): se usa para crear diagramas de dispersión

# Explicación gráficas:

1. Diagrama de barras:

Un diagrama de barras sirve para podemos comparar los distintos pesos de las naranjas, es decir, para ver que peso se repite mas o para ver la cantidad de naranjas que hay de un peso en concreto.

2. Diagrama de sectores:

Un diagrama de sectores es un tipo de diagrama en forma de círculo que sirve para representar datos estadísticos, que quedan representados en forma de sectores: Cada dato queda representado en un sector, el cual es proporcional a la frecuencia. Aquí podemos responder visualmente la pregunta de cuantas naranjas pesan menos de 130 y ver el porcentaje de esto mismo

3. Diagrama de dispersión

El diagrama de dispersión se usa comúnmente para mostrar cómo dos variables se relacionan entre sí. De este modo, permite estudiar las relaciones que existen entre dos factores, problemas o causas relacionadas con la calidad, o un problema de calidad y su posible causa.