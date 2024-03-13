import pandas as pd

def calidad(parametro, nombre_parametro): 
    if nombre_parametro == 'RMS':
        if parametro <= 0.15: 
            return 'A'
        elif 0.15 < parametro <= 0.30: 
            return 'B'
        elif 0.30 < parametro <= 0.50:
            return 'C'
        else: 
            return 'D'
    elif nombre_parametro == 'ERH':
        if parametro <= 1.0: 
            return 'A'
        elif 1.0 < parametro <= 2.5: 
            return 'B'
        elif 2.5 < parametro <= 5.0: 
            return 'C'
        elif pd.isnull(parametro):  # Verificar si el valor es NaN
            return "FF"
        else: 
            return 'D'
    elif nombre_parametro == 'ERZ':
        if parametro <= 2.0: 
            return 'A'
        elif 2.0 < parametro <= 5.0:
            return 'B'
        elif pd.isnull(parametro):  # Verificar si el valor es NaN
            return "FF"
        else: 
            return 'C'
    elif nombre_parametro == 'GAP':
        if parametro <= 90: 
            return 'A'
        elif 50 < parametro <= 135: 
            return 'B'
        elif 135 < parametro <= 180: 
            return 'C'
        else: 
            return 'D'
    elif nombre_parametro=='NST': 
        if parametro>=6:
            return 'A'
        else: 
            return 'D'


# Importar el archivo con todos los parámetros del DataFrame
rutaa = r'RIA_parametros.csv' 
df = pd.read_csv(rutaa)

# Convertir las columnas ERH y ERZ a números
df['ERH'] = pd.to_numeric(df['ERH'], errors='coerce')
df['ERZ'] = pd.to_numeric(df['ERZ'], errors='coerce')

# Utilizar la función para calcular los qs y qn de cada parámetro
for indice, fila in df.iterrows():
    qs_rms = calidad(fila['RMS'], 'RMS')
    qs_ERH = calidad(fila['ERH'], 'ERH')
    qs_ERZ = calidad(fila['ERZ'], 'ERZ')
    qn_NST = calidad(fila['NST'], 'NST')
    qn_GAP = calidad(fila['GAP'], 'GAP')

    # Agregar las calificaciones individuales como columnas en el DataFrame
    df.at[indice, 'qs_rms'] = qs_rms
    df.at[indice, 'qs_ERH'] = qs_ERH
    df.at[indice, 'qs_ERZ'] = qs_ERZ
    df.at[indice, 'qn_NST'] = qn_NST
    df.at[indice, 'qn_GAP'] = qn_GAP

# Guardar el DataFrame en un archivo CSV
df.to_csv('qsqn.csv', index=False)
print("El test de calidad se ha realizado exitosamente.")


