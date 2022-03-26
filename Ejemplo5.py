import pandas as pd
import numpy as np

#---------------- Ejercicio A ------------------------------

data = pd.DataFrame(np.array([['Enero','Febrero','Marzo'],
                       [40000,35000,50000],
                       [56000,60000,25000],
                       [80000,70000,55000]]))
print(data)

#---------------- Ejercicio B ------------------------------

print('Numero de filas y columnas: ' ,data.shape)
print('Filas: ' ,len(data.index))
print('Columnas: ' ,len(data.count()))

#---------------- Ejercicio C ------------------------------

data2 = pd.DataFrame(np.array([
                       [40000,35000,50000],
                       [56000,60000,25000],
                       [80000,70000,55000]]))
print("ARREGLOS NÚMERO CON LAS VENTAS DEL PRIMER TRIMESTRE")
print(data2)
print('-------------Estadísticas General del DataFrame----------------------')
print(data2.describe())
print('---------Media-------- ')
print(data2.mean())
print('--------Correlación del DataFrame--------')
print(data2.corr())
print('--------Más bajo-------- ')
print(data2.min())
print('--------Más alto--------')
print(data2.max())
print('--------Mediana--------')
print(data2.median())
print('--------Desviación estandar--------')
print(data2.std())
print('--------Primera Columna--------')
print(data2[0])
print('--------Dos columnas--------')
print(data2[[0,1]])
print('--------Primera fila y última Columna--------')
print(data2.iloc[0] [2])
print('--------Primera fila--------')
print(data2.loc[0])
print(data2.iloc[0,:])