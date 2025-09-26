# Para poder usar una biblioteca en python debemos importarla
import pandas as pd
import numpy as np

print("Proyecto de análisis de datos")

archivo_excel = "datos_prueba.xlsx"  # Guardar el archivo de excel en mi variable archivo_excel

#Leemos el archivo de excel
df = pd.read_excel(archivo_excel)

# df es la variable que contiene el DataFrame
# Un DataFrame es una estructura de datos bidimensional, es decir, que tiene filas y columnas


# Imprimimos en pantalla el nombre del archivo y el contenido del DataFrame
print(archivo_excel)
print(df) 

# Vamos a validar que tipo de variable es df
print(type(df))


# DataFrame está compuesto por filas y columnas
# para poder contabilizar el número de filas y columnas utilizamos las método shape (filas, columnas)
filas, columnas = df.shape

print(f"El DataFrame tiene {filas} filas y {columnas} columnas")

print(df.head(5)) # Muestra las primeras 5 filas del DataFrame
print(df.tail(5)) # Muestra las últimas 5 filas del DataFrame

# Vamos a usar El enumerate para recorrer las columnas del DataFrame y mostrar su índice y nombre

for i, valor_col in enumerate(df.columns, start = 1):
    print(f"Columnna {i}: {valor_col}")

#Bloque 2 - Explorar filas, columnas y tipos de datos

# Contar cuantas filas tiene el DataFrame, usando el método len() para contar las filas
print(f"El numero total de filas es: {len(df)}", end="\n\n")

# Mostrar una columna por nombre de columna
print(df["Profesional"].head(20), end="\n\n") # Muestra las primeras 20 filas de la columna "Profesional"

print(df["Forma de pago"].head(20), end="\n\n")

# mostrar varias columnas por nombre de columna
print(df[["Forma de pago", "Valor atención", "Profesional"]].head(20), end="\n\n")

# Mostrar como acceder a una fila, con el método iloc (index location)
print(df.iloc[6]) # Muestra la fila 6 del DataFrame
# iloc también puede recibir un rango de filas

# De esta forma mostramos el valor de una celda específica
print(df.iloc[3, 2], end="\n\n") # Muestra el valor de la fila 3 y columna 2

# Mostrar los tipos de datos de cada columna con el atributo dtypes
print(df.dtypes) # Muestra los tipos de datos de cada columna

print(type(df.iloc[3, 3]), end="\n\n") # Muestra el tipo de dato de la celda en la fila 3 y columna 3


























