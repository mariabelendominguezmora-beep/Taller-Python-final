import pandas as pd

datos = pd.read_csv('data/personas.csv')

datos["profesion"] = datos["profesion"].astype(str)

datos["profesion"] = datos["profesion"].str.replace(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ\s]', '', regex=True)

datos["profesion"] = datos["profesion"].str.strip()

datos["profesion"] = datos["profesion"].str.title()

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

# contar profesiones únicas
cantidad = datos["profesion"].nunique()

print("Cantidad de profesiones únicas:", cantidad)