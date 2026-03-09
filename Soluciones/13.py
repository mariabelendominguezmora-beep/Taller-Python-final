import pandas as pd

df = pd.read_csv("data/personas.csv")

# Contar registros donde el salario tiene caracteres que no son números
cantidad = df["salario"].apply(lambda x: not str(x).isdigit()).sum()

print(f"Existen {cantidad} registros con caracteres no numéricos en el campo salario.")