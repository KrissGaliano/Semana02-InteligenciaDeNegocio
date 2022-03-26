import pandas as pd

ventas1 = {'Meses':['Enero','Febrero','Marzo','Abril','Mayo','Junio'],
          'Monto':[23000,45000,40000,35000,76000,50000]}


ventas2 = {'Meses':['Enero','Febrero','Marzo','Abril','Mayo','Junio'],
          'Monto':[70000,55000,64000,80000,25000,44000]}

data1 = pd.DataFrame(ventas1)
data2 =pd.DataFrame(ventas2)

datos = data1.add(data2)

print("------------DATOS DE LOS ARREGLOS-----------")

print("-------ARREGLO VENTAS 1-------")

print(data1)
print("-------ARREGLO VENTAS 2-------")
print(data2)
print("-------ARREGLO 2 SOBRE EL ARREGLO 1-------")
print(datos)