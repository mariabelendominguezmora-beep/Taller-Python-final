import pandas as pd

datos = pd.read_csv('data/personas.csv')

datos["ciudad"] = datos["ciudad"].astype(str)

datos["ciudad"] = datos["ciudad"].str.replace(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ\s]', '', regex=True)

datos["ciudad"] = datos["ciudad"].str.strip()

datos["ciudad"] = datos["ciudad"].str.title()

# contar Medellin
cantidad = (datos["ciudad"] == "Medellin").sum()

print("Registros con ciudad Medellin después de limpiar:", cantidad)