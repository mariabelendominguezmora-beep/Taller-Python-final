import pandas as pd
import codecs
import re

df = pd.read_csv('data/personas.csv', dtype=str)
df['nombre'] = df['nombre_cifrado'].apply(lambda x: codecs.decode(str(x).strip(), 'rot_13'))
df['profesion_limpia'] = df['profesion'].apply(
    lambda s: re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]', '', str(s)).strip().title()
)

cantidad = ((df['nombre'] == 'Ana') & (df['profesion_limpia'] == 'Medico')).sum()
print(f"Registros con nombre 'Ana' y profesión 'Medico': {cantidad}")
# Respuesta: 170