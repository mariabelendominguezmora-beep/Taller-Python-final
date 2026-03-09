import pandas as pd

datos = pd.read_csv('data/personas.csv')

datos["ciudad"] = datos["ciudad"].astype(str)

datos["ciudad"] = datos["ciudad"].str.replace(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ\s]', '', regex=True)

datos["ciudad"] = datos["ciudad"].str.strip()

datos["ciudad"] = datos["ciudad"].str.title()

# contar ciudades únicas
cantidad = datos["ciudad"].nunique()

print("Cantidad de ciudades únicas:", cantidad)