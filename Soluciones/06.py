import pandas as pd

datos = pd.read_csv('data/personas.csv')

datos["ciudad"] = datos["ciudad"].astype(str)

datos["ciudad"] = datos["ciudad"].str.replace(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ\s]', '', regex=True)

datos["ciudad"] = datos["ciudad"].str.strip()

datos["ciudad"] = datos["ciudad"].str.title()

# contar Bogota
cantidad = (datos["ciudad"] == "Bogota").sum()

print("Registros con ciudad Bogota después de limpiar:", cantidad)