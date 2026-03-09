import pandas as pd
import codecs

df = pd.read_csv('data/personas.csv', dtype=str)
df['nombre'] = df['nombre_cifrado'].apply(lambda x: codecs.decode(str(x).strip(), 'rot_13'))
df['apellido'] = df['apellido_cifrado'].apply(lambda x: codecs.decode(str(x).strip(), 'rot_13'))

cantidad = ((df['nombre'] == 'Jose') & (df['apellido'] == 'Garcia')).sum()
print(f"Registros con nombre 'Jose' y apellido 'Garcia': {cantidad}")
# Respuesta: 96