import numpy as np
import pandas as pd

# Define el tamaño del conjunto de datos
tamaño_dataset = 10000

# Define el porcentaje real de hombres en la población
porcentaje_hombres_real = 0.505  # Por ejemplo, el 50.5% son hombres

# Calcula el número de hombres en el conjunto de datos sintético
num_hombres = int(tamaño_dataset * porcentaje_hombres_real)

# Crea una columna "sexo" con la proporción correcta
hombres = np.ones(num_hombres)  # 1 representa "hombre"
mujeres = np.zeros(tamaño_dataset - num_hombres)  # 0 representa "mujer"

# Combina las dos listas para obtener la columna completa de "sexo"
columna_sexo = np.concatenate([hombres, mujeres])

# Mezcla los valores para que no estén en orden
np.random.shuffle(columna_sexo)

# Crea un DataFrame con la columna "sexo" y cualquier otra información que desees agregar
data = pd.DataFrame({'sex': columna_sexo})
data['sex'] = data['sex'].astype(int)

# Define el porcentaje de fumadores para hombres y mujeres
porcentaje_fumadores_hombres = 0.367
porcentaje_fumadores_mujeres = 0.078

data['smoker'] = np.where(data['sex'] == 1, np.random.choice([0, 1], size=tamaño_dataset, p=[1 - porcentaje_fumadores_hombres, porcentaje_fumadores_hombres]),
                          np.random.choice([0, 1], size=tamaño_dataset, p=[1 - porcentaje_fumadores_mujeres, porcentaje_fumadores_mujeres]))


# Define el porcentaje de fumadores para hombres y mujeres
porcentaje_PCR_hombres = 0.024
porcentaje_PCR_mujeres = 0.029


# Agrega la columna "fumador" al DataFrame
data['result PCR mycoplasma'] = np.where(data['sex'] == 1, np.random.choice([0, 1], size=tamaño_dataset, p=[1 - porcentaje_PCR_hombres, porcentaje_PCR_hombres]),
                          np.random.choice([0, 1], size=tamaño_dataset, p=[1 - porcentaje_PCR_mujeres, porcentaje_PCR_mujeres]))

print(data.to_string())
