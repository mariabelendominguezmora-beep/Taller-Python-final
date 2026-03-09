import pandas as pd

df = pd.read_csv("data/personas.csv")

# Limpiar ciudad
df["ciudad"] = (
    df["ciudad"]
    .astype(str)
    .str.replace(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ\s]', '', regex=True)
    .str.strip()
    .str.title()
)

# Limpiar profesion
df["profesion"] = (
    df["profesion"]
    .astype(str)
    .str.replace(r'[^A-Za-zÁÉÍÓÚáéíóúÑñ\s]', '', regex=True)
    .str.strip()
    .str.title()
)

# Filtrar ingenieros
ingenieros = df[df["profesion"] == "Ingeniero"]

# Contar ingenieros por ciudad
resultado = ingenieros["ciudad"].value_counts().idxmax()

print(f"La ciudad con más ingenieros es: {resultado}")