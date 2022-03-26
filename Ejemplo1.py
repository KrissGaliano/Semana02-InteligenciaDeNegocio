import pandas as pd
import numpy as np

#-------------------EJERCICIO 01----------------------------

data = pd.Series(['Enero', 'Febrero','Marzo','Abril','Mayo','Junio'],
                 index=[1,2,3,4,5,6])
print("Respuesta de la A: ")
print(data)

#-------------------EJERCICIO 02----------------------------

data2 = pd.Series({'Enero':40000,'Febrero':35000, 'Marzo':50000})

print("Respuesta de la B: ")
print(data2)

#---------------------EJERCICIO 03 ¿------------------------------

data3 = pd.Series(np.random.randn(10))
print("Respuesta de la C: ")
print(data3)
print(data3.head())
print(data3.tail())
print(data3.head(2))
print(data3.tail(2))

#---------------------EJERCICIO 04---------------------------------

