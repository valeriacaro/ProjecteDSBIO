import numpy as np
import pandas as pd

# Define el tamaño del conjunto de datos
tamaño_dataset = 10000

# Define el porcentaje real de hombres en la población
porcentaje_hombres_real = 0.505  # Por ejemplo, el 50.5% son hombres

# Calcula el número de hombres en el conjunto de datos sintético
num_hombres = int(tamaño_dataset * porcentaje_fumadores_real)

# Crea una columna "sexo" con la proporción correcta
hombres = np.ones(num_fumadores)  # 1 representa "hombre"
mujeres = np.zeros(tamaño_dataset - num_fumadores)  # 0 representa "mujer"

# Combina las dos listas para obtener la columna completa de "sexo"
columna_sexo = np.concatenate([hombres, mujeres])

# Mezcla los valores para que no estén en orden
np.random.shuffle(columna_sexo)

# Crea un DataFrame con la columna "sexo" y cualquier otra información que desees agregar
data = pd.DataFrame({'sex': columna_sexo})

# Define el porcentaje de fumadores para hombres y mujeres
porcentaje_fumadores_hombres = 0.367
porcentaje_fumadores_mujeres = 0.078

# Calcula el número de fumadores para hombres y mujeres
num_fumadores_hombres = int(num_hombres * porcentaje_fumadores_hombres)
num_fumadores_mujeres = int((tamaño_dataset - num_hombres) * porcentaje_fumadores_mujeres)

# Crea las listas de fumadores para hombres y mujeres
fumadores_hombres = np.ones(num_fumadores_hombres)
fumadores_mujeres = np.ones(num_fumadores_mujeres)

# Crea las listas de no fumadores para hombres y mujeres
no_fumadores_hombres = np.zeros(num_hombres - num_fumadores_hombres)
no_fumadores_mujeres = np.zeros((tamaño_dataset - num_hombres) - num_fumadores_mujeres)

# Combina las listas para obtener las columnas completas de "fumador" para hombres y mujeres
columna_fumador_hombres = np.concatenate([fumadores_hombres, no_fumadores_hombres])
columna_fumador_mujeres = np.concatenate([fumadores_mujeres, no_fumadores_mujeres])

# Mezcla los valores para que no estén en orden
np.random.shuffle(columna_fumador_hombres)
np.random.shuffle(columna_fumador_mujeres)

# Agrega la columna "fumador" al DataFrame
data['fumador'] = np.where(data['sexo'] == 1, columna_fumador_hombres, columna_fumador_mujeres)

# Puedes imprimir el DataFrame resultante
print(data.head())
