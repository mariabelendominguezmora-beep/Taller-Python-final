#cargar datos
import pandas as pd 
import codecs 

datos = pd.read_csv('data/personas.csv')
#######-------carga de datos------#####
####----FIN----##3

texto_original = 'Juan'

# cifrar (ROT 13)
texto_cifrado = codecs.encode (texto_original,'rot_13')
print (f'cifrado: {texto_cifrado}')

#Juan = Whna

condicion= datos ['nombre_cifrado']=='Whna'
datos_nuevos= datos [condicion]
print('el numero de repeticiones de Juan es:', datos_nuevos.shape[0])


