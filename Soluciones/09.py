import pandas as pd
import re

df = pd.read_csv('data/personas.csv', dtype=str)
df['profesion_limpia'] = df['profesion'].apply(
    lambda s: re.sub(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]', '', str(s)).strip().title()
)

cantidad = (df['profesion_limpia'] == 'Ingeniero').sum()
print(f"Registros con profesión 'Ingeniero': {cantidad}")