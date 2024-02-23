#Dulce Abril González 
# Introducción al programa
print("********************************************")
print("*  Bienvenido a la Clasificación de Sismos  *")
print("*    en Función de su Profundidad (CSP)    *")
print("********************************************")
print("")
print(" Para la clasificación se utilizan los siguientes parámetros:")
print(" 0 < h ≤ 25   ---   Cortical")
print(" 25 < h ≤ 60  ---   Subducción interfase")
print(" h > 60       ---   Subducción intraplaca")
print("")


import pandas as pd

# Cargar el archivo CSV en un DataFrame
ruta = r'reporte_info_all_2023.csv'
df = pd.read_csv(ruta)

# Crear una nueva columna "tipo" basada en la columna "depth"
df['clasificación'] = df['DEPTH'].apply(lambda x: 'cortical' if x <= 25 else ('subducción interfase' if x > 25 and x <= 60 else 'subducción intraplaca'))

# Guardar el DataFrame modificado en un nuevo archivo CSV
ruta_nueva = r'reporte_info_all_2023_clasificados.csv'
df.to_csv(ruta_nueva, index=False)

#mostrarle al usuario el resultado de la clasificación
print("A continuación una pequeña muestra que recopila columnas de identificación y aquellas usadas para hacer la clasificación en este script. :)")
print("")
print(df[['NO', 'ID', 'DEPTH', 'clasificación']].head())
