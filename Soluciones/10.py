import pandas as pd

datos = pd.read_csv('data/personas.csv')

# convertir a string
datos["profesion"] = datos["profesion"].astype(str)

# quitar caracteres anormales
datos["profesion"] = datos["profesion"].str.replace(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ\s]', '', regex=True)

# quitar espacios
datos["profesion"] = datos["profesion"].str.strip()

# normalizar formato
datos["profesion"] = datos["profesion"].str.title()

# corregir profesiones con vocales faltantes
datos["profesion"] = datos["profesion"].replace({
    "Ingniero": "Ingeniero",
    "Ingnero": "Ingeniero",
    "Prgramador": "Programador",
    "Programdor": "Programador",
    "Medco": "Medico",
    "Abgdo": "Abogado",
    "Cntador": "Contador",
    "Arqutecto": "Arquitecto"
})

# contar Programadores
cantidad = (datos["profesion"] == "Programador").sum()

print("Cantidad de Programadores:", cantidad)