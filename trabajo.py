import numpy as np

archivo = open("/content/drive/MyDrive/Colab Notebooks/datos climaticos.txt", "r")

stgo_matrix = np.zeros((12, 2))# Crea una matriz de ceros de tamaño 12x2 para almacenar los datos climáticos de Santiago
valpo_matrix = np.zeros((12, 2))# Crea una matriz de ceros de tamaño 12x2 para almacenar los datos climáticos de Valparaíso
pta_matrix = np.zeros((12, 2))# Crea una matriz de ceros de tamaño 12x2 para almacenar los datos climáticos de Punta Arenas
lineas = archivo.readlines() # Lee todas las líneas del archivo y las almacena en la lista 'lineas'
print(lineas)

ciudad = "" # Inicializa la variable 'ciudad' para almacenar el nombre de la ciudad actual

# Itera sobre cada línea del archivo de datos climáticos
for linea in lineas:

    # Comprueba el nombre de la ciudad en la línea actual y actualiza la variable 'ciudad'
    if linea.split(" ")[0] == "Santiago":
        ciudad = "stgo"  # Ciudad actual es Santiago
        indice = -3  # Inicializa el índice para almacenar datos en la matriz correspondiente
    elif linea.split(" ")[0] == "Valparaiso":
        ciudad = "valpo"  # Ciudad actual es Valparaíso
        indice = -3  # Inicializa el índice para almacenar datos en la matriz correspondiente
    elif linea.split(" ")[0] == "Punta":
        ciudad = "pta"  # Ciudad actual es Punta Arenas
        indice = -3  # Inicializa el índice para almacenar datos en la matriz correspondiente

    # Comprueba la ciudad actual y asigna los datos climáticos a la matriz correspondiente
    if ciudad == "stgo":
        indice = indice + 1  # Incrementa el índice para almacenar en la siguiente fila de la matriz
        if indice >= 0 and indice < 12:  # Verifica que el índice esté dentro del rango válido
            # Almacena la temperatura y humedad en la matriz de Santiago
            stgo_matrix[indice][0] = linea.split(" ")[1].strip()
            stgo_matrix[indice][1] = linea.split(" ")[2].strip()
    elif ciudad == "valpo":
        indice = indice + 1  # Incrementa el índice para almacenar en la siguiente fila de la matriz
        if indice >= 0 and indice < 12:  # Verifica que el índice esté dentro del rango válido
            # Almacena la temperatura y humedad en la matriz de Valparaíso
            valpo_matrix[indice][0] = linea.split(" ")[1].strip()
            valpo_matrix[indice][1] = linea.split(" ")[2].strip()
    elif ciudad == "pta":
        indice = indice + 1  # Incrementa el índice para almacenar en la siguiente fila de la matriz
        if indice >= 0 and indice < 12:  # Verifica que el índice esté dentro del rango válido
            # Almacena la temperatura y humedad en la matriz de Punta Arenas
            pta_matrix[indice][0] = linea.split(" ")[1].strip()
            pta_matrix[indice][1] = linea.split(" ")[2].strip()

print("Santiago:")
for row in stgo_matrix:
    print("\t".join(map(str, row)))
print("\nValparaiso:")
for row in valpo_matrix:
    print("\t".join(map(str, row)))
print("\nPunta Arenas:")
for row in pta_matrix:
    print("\t".join(map(str, row)))

combinada = np.concatenate((stgo_matrix, valpo_matrix, pta_matrix), axis=0)
print(combinada)

suma_indices_1 = np.sum(combinada[:, 1])
print("Cantidad de agua caída en Chile",suma_indices_1, "mm")

#calcula trimestre 1

trim1_stgo = np.sum(stgo_matrix[0:3, 0])# Calcula la suma de las temperaturas para el primer trimestre en Santiago
trim1_val = np.sum(valpo_matrix[0:3, 0])# Calcula la suma de las temperaturas para el primer trimestre en Valparaíso
trim1_pta = np.sum(pta_matrix[0:3, 0]) # Calcula la suma de las temperaturas para el primer trimestre en Punta Arenas
trim1_total = (trim1_stgo + trim1_val + trim1_pta)/9 # Calcula el promedio de las temperaturas del primer trimestre para todas las ciudades y la amacena en "trim1_total"

# Calcula trimestre 2
trim2_stgo = np.sum(stgo_matrix[3:6, 0])  # Calcula la suma de las temperaturas para el segundo trimestre en Santiago
trim2_val = np.sum(valpo_matrix[3:6, 0])  # Calcula la suma de las temperaturas para el segundo trimestre en Valparaíso
trim2_pta = np.sum(pta_matrix[3:6, 0])   # Calcula la suma de las temperaturas para el segundo trimestre en Punta Arenas
trim2_total = (trim2_stgo + trim2_val + trim2_pta) / 9  # Calcula el promedio de las temperaturas del segundo trimestre para todas las ciudades y la amacena en "trim2_total"

# Calcula trimestre 3
trim3_stgo = np.sum(stgo_matrix[6:9, 0])  # Calcula la suma de las temperaturas para el tercer trimestre en Santiago
trim3_val = np.sum(valpo_matrix[6:9, 0])  # Calcula la suma de las temperaturas para el tercer trimestre en Valparaíso
trim3_pta = np.sum(pta_matrix[6:9, 0])   # Calcula la suma de las temperaturas para el tercer trimestre en Punta Arenas
trim3_total = (trim3_stgo + trim3_val + trim3_pta) / 9  # Calcula el promedio de las temperaturas del tercer trimestre para todas las ciudades y la amacena en "trim3_total"

# Calcula trimestre 4
trim4_stgo = np.sum(stgo_matrix[9:12, 0])  # Calcula la suma de las temperaturas para el cuarto trimestre en Santiago
trim4_val = np.sum(valpo_matrix[9:12, 0])  # Calcula la suma de las temperaturas para el cuarto trimestre en Valparaíso
trim4_pta = np.sum(pta_matrix[9:12, 0])   # Calcula la suma de las temperaturas para el cuarto trimestre en Punta Arenas
trim4_total = (trim4_stgo + trim4_val + trim4_pta) / 9  # Calcula el promedio de las temperaturas del cuarto trimestre para todas las ciudades y la amacena en "trim4_total"

# Resultados
print("Temperatura promedio trimestre 1:", trim1_total, "(°C)")
print("Temperatura promedio trimestre 2:", trim2_total, "(°C)")
print("Temperatura promedio trimestre 3:", trim3_total, "(°C)")
print("Temperatura promedio trimestre 4:", trim4_total, "(°C)")

# Máxima y mínima posición de temperaturas en combinada
max_temp_pos = np.argmax(combinada[:, 0])  # Encuentra la posición de la temperatura máxima en combinada(Devuelve los índices de los valores máximos a lo largo de un eje.)
min_temp_pos = np.argmin(combinada[:, 0])  # Encuentra la posición de la temperatura mínima en combinada(Devuelve los índices de los valores minimos a lo largo de un eje.)

# Definición de ciudades para las temperaturas máxima y mínima
alta_temp_ciudad = ""  # Variable para almacenar la ciudad con la temperatura máxima
baja_temp_ciudad = ""  # Variable para almacenar la ciudad con la temperatura mínima

# Determinar la ciudad para la temperatura máxima
if max_temp_pos < 12:  # Si la posición de la temperatura máxima está en las primeras 12 filas de combinada
  alta_temp_ciudad = "Santiago"  # La ciudad con la temperatura máxima es Santiago
elif max_temp_pos < 24:  # Si la posición de la temperatura máxima está entre las filas 12 y 24 de combinada
  alta_temp_ciudad = "Valparaiso"  # La ciudad con la temperatura máxima es Valparaíso
else:  # Si la posición de la temperatura máxima está más allá de la fila 24 de combinada
  alta_temp_ciudad = "Punta Arenas"  # La ciudad con la temperatura máxima es Punta Arenas

# Determinar la ciudad para la temperatura mínima
if min_temp_pos < 12:  # Si la posición de la temperatura mínima está en las primeras 12 filas de combinada
  baja_temp_ciudad = "Santiago"  # La ciudad con la temperatura mínima es Santiago
elif min_temp_pos < 24:  # Si la posición de la temperatura mínima está entre las filas 12 y 24 de combinada
  baja_temp_ciudad = "Valparaiso"  # La ciudad con la temperatura mínima es Valparaíso
else:  # Si la posición de la temperatura mínima está más allá de la fila 24 de combinada
  baja_temp_ciudad = "Punta Arenas"  # La ciudad con la temperatura mínima es Punta Arenas

# Impresión de las temperaturas máxima y mínima con sus respectivas ciudades
print("Máxima temperatura en 2022:", combinada[max_temp_pos, 0], "°C en", alta_temp_ciudad)  # Imprime la temperatura máxima y su ciudad
print("Mínima temperatura en 2022:", combinada[min_temp_pos, 0], "°C en", baja_temp_ciudad)  # Imprime la temperatura mínima y su ciudad
