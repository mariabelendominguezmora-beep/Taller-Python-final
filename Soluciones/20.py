import pandas as pd

df = pd.read_csv("data/personas.csv")

# Convertir la columna fecha_nacimiento a formato fecha
df["fecha_nacimiento"] = pd.to_datetime(
    df["fecha_nacimiento"],
    errors="coerce"
)

# Filtrar personas nacidas entre 1990 y 2000
personas = df[
    (df["fecha_nacimiento"].dt.year >= 1990) &
    (df["fecha_nacimiento"].dt.year <= 2000)
]

# Contar registros
cantidad = personas.shape[0]

print(f"Existen {cantidad} personas nacidas entre 1990 y 2000.")