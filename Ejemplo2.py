import pandas as pd

ventas = {'Meses':['Enero','Febrero','Marzo','Abril','Mayo','Junio'],
          'Monto':[23000,45000,40000,35000,76000,50000]}
#---Ejemplo A---------
data = pd.DataFrame(ventas)
print("La Respuesta de la A es: ")
print(data)

#----Ejemplo B--------
data2 = pd.DataFrame(ventas,columns=['Monto','Meses'])
print("La Respuesta de la B es: ")
print(data2)