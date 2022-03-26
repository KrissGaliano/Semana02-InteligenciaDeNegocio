import pandas as pd

archivo = pd.read_excel('Ventas02.xlsx',sheet_name='Ventas',skiprows=1)

print(archivo)