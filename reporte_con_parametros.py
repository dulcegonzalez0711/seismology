import numpy as np 
import pandas as pd 

#Calcular los valores para error horizontal en epicentro 
def calcular_ERH(SDX, SDY): 
    if not isinstance(SDX, (int, float)) or not isinstance(SDY, (int, float)):
        return "desconocido"
    sqsum=np.square(SDX)+np.square(SDY)
    ERH=np.sqrt(sqsum)
    return round(ERH,2)

#importar los datos desde el informe estableciendo ruta
ruta = r'Reporte_IA.csv'
df = pd.read_csv(ruta)

#indexar los valores de error vertical
df['ERZ'] = df['dp_e']

df['GAP']=df['GAP'].apply(lambda x: x.strip())
df['long_e']=df['long_e'].apply(lambda x: x.strip())
df['lat_e']=df['lat_e'].apply(lambda x: x.strip())

#hacer data cleaning con las filas que están vacías 
df['lat_e'] = pd.to_numeric(df['lat_e'], errors='coerce')
df['long_e'] = pd.to_numeric(df['long_e'], errors='coerce')

erh_values=[]
#indexar los valores de error en horizontal 
for indice, fila in df.iterrows(): 
    ERH=calcular_ERH(fila['lat_e'], fila['long_e'])
    erh_values.append(ERH)

df['ERH']=erh_values
print(df[['NO', 'ID', 'ERZ', 'ERH', 'GAP']].head())
df.to_csv('RIA_parametros.csv', index=False)



